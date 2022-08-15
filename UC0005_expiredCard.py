from typing import Union

from TCs.fdwk_prefs_BtA import test_case_user_setup
from common import *

def sudo_cardDelivered_notification():
    sudo_notification("sudo kate pošli mi pušku na odeslání karty poštou")

def wait_for_and_click_cardDelivered_notification():
    wait_for_and_click_notification("Vaše karta právě míří na poštu. Brzy ji najdete ve schránce.")

def cardDelivered_test_setup():
    test_case_user_setup(UserType.advanced)
    sudo_cardDelivered_notification()


def sudo_cardSent_notification():
    sudo_notification("sudo kate pošli mi pušku na doručení karty")

def wait_for_and_click_cardSent_notification():
    wait_for_and_click_notification("Vaše nová platební karta už je připravena na pobočce, tak ji nenechte dlouho čekat.")   

def cardSent_test_setup():
    test_case_user_setup(UserType.advanced)
    sudo_cardSent_notification()


def sudo_expiredCard_notification():
    sudo_notification("sudo kate pošli mi pušku na expiraci karty")    

def wait_for_and_click_expiredCard_notification():
    wait_for_and_click_notification("Blíží se konec platnosti vaší karty. Chcete novou poslat domů nebo si ji raději vyzvednete na pobočce?")

def expiredCard_test_setup():
    test_case_user_setup(UserType.advanced)
    sudo_expiredCard_notification()    



postmail_address: Union[str, None] = None

@TestSuite
@labels("DoKapsy") #, "Smart")
@TC_setup(expiredCard_test_setup)
class UC0005_expiredCard:
    @ordered
    def send_by_postmail__address_change_with_mistakes():
        # 1. in address picker; 2. confirming adress pick; 3. picked adress at the begining of the flow. (only needed for confirmed address)
        addresses: list[list[str]] = [
            [
                "Zbraslavská 37 Dolní Břežany, 25241",
                "Zbraslavská 37, Dolní Břežany, 25241"
            ],
            [
                "Zbraslavská 37 Jesenice, 25242",
                "Zbraslavská 37, Jesenice, 25242",
                "ZBRASLAVSKÁ 37\n25242 JESENICE"
            ],
            [
                "Zbraslavská 37/1 Praha 5 - Malá Chuchle, 15900",
                "Zbraslavská 37/1, Praha 5 - Malá Chuchle, 15900"
            ],
            [
                "Zbraslavská 39/37 Praha 5 - Malá Chuchle, 15900",
                "Zbraslavská 39/37, Praha 5 - Malá Chuchle, 15900",
                "Zbraslavská 39/37\n15900 PRAHA 5 - MALÁ CHUCHLE"
            ],
        ]
        
        wait_for_and_click_expiredCard_notification()

        qabs = Steps_expired.first()
        qabs.click(1)   # click on qabs "Poslat poštou"

        # Going through this UC (maybe including other testers with other users (card is the same)),
        #   changes the address, so we don't know, what will we get.
        # So we run this TCs in specified order and remember the address from now one.
        global postmail_address
        if postmail_address is None:
            wait_for_one_of_QABs(["Ano", "Ne, není"])
            found_texts, _ = get_text_children(find_chat_root())
            postmail_address = found_texts[1].text.removeprefix("Gabriela Zběsilá\n")
            if postmail_address == addresses[0 + 1][2]:
                index = 2
            else:
                index = 0

        qabs = expecting(
            [   
                "Jen pro jistotu. Je tohle správná adresa?",
                f"Gabriela Zběsilá\n{postmail_address}"
            ],
            ["Ano", "Ne, není"]
        )
        qabs.click(2)   # click on qabs "Ne, není"

        enter_address_text = "Prosím, zadejte adresu, na kterou chcete svou kartu poslat."
        expecting([enter_address_text])

        
        # nenaslo ziadnu moznost
        send_answer("TUTANCHAMON, austerlitz")
        expecting([
            "Zadanou adresu se mi nepodařilo najít. Prosím, zkuste upravit zadání. Nejlépe ve formátu \"ulice ČP, město\" (např. \"Výmolova 329, Praha\" nebo \"Křečovice 12\").",
            enter_address_text
        ])


        # prilis vela moznosti
        send_answer("Zbraslavská, Praha")
        expecting([
            "Našla jsem příliš mnoho adres. Prosím, upravte zadání. Nejlépe ve formátu \"ulice ČP, město\" (např. \"Výmolova 329, Praha\" nebo \"Křečovice 12\").",
            enter_address_text
        ])


        # dobra moznost - Opravit
        send_answer("Zbraslavská 36")
        qabs = expecting(
            [
                "Zbraslavská 36 Jesenice, 25242",
                "Zbraslavská 36/3 Praha 5 - Malá Chuchle, 15900",
            ],
            ["Opravit"]
        )

        qabs.click(1) # Opravit
        expecting([enter_address_text])


        # dobra moznost - vybrat adresu - Upravit
        send_answer("Zbraslavská 37")
        qabs = expecting(
            addresses,
            ["Opravit"]
        )

        click_button(addresses[index][0])
        qabs = expecting(
            [f"Odeslat na adresu {addresses[index][1]}?"],
            ["Ano", "Upravit"]
        )

        qabs.click(2) # Upravit
        expecting([enter_address_text])


        # dobra moznost - vybrat adresu - ano
        send_answer("Zbraslavská 37")
        qabs = expecting(
            addresses,
            ["Opravit"]
        )

        click_button(addresses[index + 1][0])
        qabs = expecting(
            [f"Odeslat na adresu {addresses[index + 1][1]}?"],
            ["Ano", "Upravit"]
        )

        qabs.click(1) # Ano

        DoKapsy_enter_security_pin()

        qabs = expecting_utterance(
            Utterance(["Skvělé. Přijde vám několik týdnů před koncem platnosti stávající karty."])
            + what_else_can_I_do_utterance
        )
        postmail_address = addresses[index + 1][2]

    @ordered
    def send_by_postmail__no_address_change():
        wait_for_and_click_expiredCard_notification()
        qabs = Steps_expired.first()
        qabs.click(1)   # click on qabs "Poslat poštou"

        # it is best to run this together with send_by_postmail__address_change_with_mistakes
        global postmail_address
        if postmail_address is None:
            wait_for_one_of_QABs(["Ano", "Ne, není"])
            found_texts, _ = get_text_children(find_chat_root())
            postmail_address = found_texts[1].text.removeprefix("Gabriela Zběsilá\n")

        qabs = expecting(
            [
                "Jen pro jistotu. Je tohle správná adresa?",
                f"Gabriela Zběsilá\n{postmail_address}"
            ],
            ["Ano", "Ne, není"]
        )
        qabs.click(1)   # click on qabs "Ano"

        qabs = expecting_utterance(
            Utterance(["Skvělé. Přijde vám několik týdnů před koncem platnosti stávající karty."])
            + what_else_can_I_do_utterance
        )


    def remind_me_later():
        wait_for_and_click_expiredCard_notification()
        
        qabs = Steps_expired.first()
        qabs.click(3)   # click on qabs "Připomeň mi to později"

        expecting_utterance(get_remind_me_later_utterance())

    def why_this():
        wait_for_and_click_expiredCard_notification()

        qabs = Steps_expired.first()
        qabs.click(5)   # Proč se mi tento tip ukázal?

        expecting_utterance(
            why_this_tip_utterance
            + Steps_expired.first_response_common_utterance
        )
    
    def no_thanks():
        wait_for_and_click_expiredCard_notification()

        qabs = Steps_expired.first()
        qabs.click(4)   # Nemám zájem

        expecting(
            ["Dobře, přeji hezký zbytek dne. ☀️"],
            ["Co dalšího umíš?"]
        )

    # @only_this
    def branch__correcting_answers__wrong_pin():
        wait_for_and_click_expiredCard_notification()

        qabs = Steps_expired.first()
        qabs.click(2)   # Vyzvednout na pobočce

        enter_PSC_text = "Prosím, zadejte PSČ, kde si chcete svou kartu vyzvednout, a pak vyberte pobočku."
        
        expecting([enter_PSC_text])
        send_answer("123")

        expecting([
            "Toto nevypadá jako poštovní směrovací číslo (PSČ).",
            enter_PSC_text
        ])
        send_answer("110 00")

        qabs = expecting(
            [
                "Revoluční 725/11, Praha 1",
                "Spálená 2121/22, Praha 1",
                "Na Příkopě 857/18, Praha 1",
                "Perlová 371/5, Praha 1",
            ],
            ["Opravit"]
        )
        qabs.click(1)  # Opravit

        expecting([enter_PSC_text])
        send_answer("12000")

        expecting(
            [
                "Anglická 140/20, Praha",
                "Bělehradská 478/110, Praha 2",
            ],
            ["Opravit"]
        )
        click_button("Bělehradská 478/110, Praha 2")

        qabs = expecting(
            ["Odeslat na pobočku Bělehradská 478/110?"],
            ["Ano", "Upravit"]
        )
        qabs.click(2) # Upravit

        expecting([enter_PSC_text])
        send_answer("13000")

        utterance_for_13000 = Utterance(
            [
                "Vinohradská 89/90, Praha 3",
                "Biskupcova 1745/7, Praha 3",
            ],
            ["Opravit"]
        )
        qabs = expecting_utterance(utterance_for_13000)
        send_answer("tada")
        
        qabs = expecting_utterance(
            Utterance(["Tady pobočku nemáme. Zadejte jiné PSČ města s pobočkou."])
            + utterance_for_13000
        )
        send_answer("Vinohradská") # Vinohradská 89/90, Praha 3

        qabs = expecting(
            ["Odeslat na pobočku Vinohradská 89/90?"],
            ["Ano", "Upravit"]
        )
        qabs.click(1)  # Ano

        if ctx.config.app_type == AppType.Smart:
            raise NotImplementedError()
        for i in range(5):
            DoKapsy_enter_security_pin(is_right_one = False)

        expecting(["Došlo k obecné chybě. Prosím zkuste to znovu později."])
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
    
    def branch__happy_path():
        wait_for_and_click_expiredCard_notification()

        qabs = Steps_expired.first()
        qabs.click(2)   # Vyzvednout na pobočce

        enter_PSC_text = "Prosím, zadejte PSČ, kde si chcete svou kartu vyzvednout, a pak vyberte pobočku."
        
        expecting([enter_PSC_text])
        send_answer("110 00")

        qabs = expecting(
            [
                "Revoluční 725/11, Praha 1",
                "Spálená 2121/22, Praha 1",
                "Na Příkopě 857/18, Praha 1",
                "Perlová 371/5, Praha 1",
            ],
            ["Opravit"]
        )
        click_button("Revoluční 725/11, Praha 1")

        qabs = expecting(
            ["Odeslat na pobočku Revoluční 725/11?"],
            ["Ano", "Upravit"]
        )
        qabs.click(1)  # Ano

        if ctx.config.app_type == AppType.Smart:
            raise NotImplementedError()
        else:
            DoKapsy_enter_security_pin(is_right_one = False)
            DoKapsy_enter_security_pin(is_right_one = True)

        expecting_utterance(
            Utterance(["Zařízeno. Dáme vám vědět, jakmile bude karta na pobočce Revoluční 725/11, Praha 1."])
            + what_else_can_I_do_utterance
        )

    

@TestSuite
@labels("DoKapsy")
@TC_setup(cardSent_test_setup)
class UC0005_cardSent:
    def ok_thanks():
        wait_for_and_click_cardSent_notification()

        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta už na vás čeká v pobočce. Tak ji nenechte dlouho čekat."
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(1)

        qabs = expecting_utterance(what_else_can_I_do_utterance)

    def remind_me_later():
        wait_for_and_click_cardSent_notification()

        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta už na vás čeká v pobočce. Tak ji nenechte dlouho čekat." 
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(2)   # klikne na QAB "Připomeň mi to později"

        expecting_utterance(get_remind_me_later_utterance())

    def Why_this():
        wait_for_and_click_cardSent_notification()

        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta už na vás čeká v pobočce. Tak ji nenechte dlouho čekat."  
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(3)   # klikne na QAB "Proč se mi tento tip ukázal?"

        qabs = expecting_utterance(
            why_this_tip_utterance
            + Utterance(
                ["Vaše karta už na vás čeká v pobočce. Tak ji nenechte dlouho čekat."],
                ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
            )
        )

@TestSuite
@labels("DoKapsy")
@TC_setup(cardDelivered_test_setup)
class UC0005_cardDelivered:
    def ok_thanks():
        wait_for_and_click_cardDelivered_notification()
        
        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta právě míří na poštu. Brzy ji najdete ve schránce."
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(1)   # klikne na QAB "Dobře, děkuji"
        
        qabs = expecting_utterance(what_else_can_I_do_utterance)
        
    def remind_me_later():
        wait_for_and_click_cardDelivered_notification()
        
        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta právě míří na poštu. Brzy ji najdete ve schránce."  
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(2)   # klikne na QAB "Připomeň mi to později"
        
        expecting_utterance(get_remind_me_later_utterance())

    def why_this():
        wait_for_and_click_cardDelivered_notification()

        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Vaše karta právě míří na poštu. Brzy ji najdete ve schránce." 
            ],
            ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
        )
        qabs.click(3)   # klikne na QAB "Proč se mi tento tip ukázal?"

        qabs = expecting_utterance(
            why_this_tip_utterance
            + Utterance(
                ["Vaše karta právě míří na poštu. Brzy ji najdete ve schránce."],
                ["Dobře, děkuji", "Připomeň mi to později", "Proč se mi tento tip ukázal?"]
            )
        )


class Steps_expired:
    first_response_common_utterance = Utterance(
        ["Všimla jsem si, že platnost vaší karty končící na 3378 vyprší již 01/25. Chcete novou poslat poštou nebo si ji raději vyzvednete na pobočce?"],
        ["Poslat poštou", "Vyzvednout na pobočce", "Připomeň mi to později", "Nemám zájem", "Proč se mi tento tip ukázal?"]
    )
    @staticmethod
    def first():
        return expecting_utterance(
            Utterance([f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate."])
            + Steps_expired.first_response_common_utterance
        )
