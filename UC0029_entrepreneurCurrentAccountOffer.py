from TCs.fdwk_prefs_BtA import test_case_user_setup
from common import *

def sudo_entrepreneurCurrentAccountOffer_notification():
    sudo_notification("sudo kate pošli mi pušku na nabídku podnikatelského konta")

def wait_for_and_click_entrepreneurCurrentAccountOffer_notification():
    wait_for_and_click_notification("Vidím, že využíváte k podnikání svůj osobní účet. Chcete zjistit víc o možnosti založení podnikatelského konta?")

def entrepreneurCurrentAccountOffer_test_setup():
    test_case_user_setup(UserType.advanced)
    sudo_entrepreneurCurrentAccountOffer_notification()

qabsText = [    
            "Jaké jsou výhody podnikatelského konta?",
            "Proč si sjednat podnikatelské konto?",
            "Můžu si konto sjednat on-line?"
    ]    

class basic_steps:
    @staticmethod
    def notification_offer():
        return expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Víte, že si u nás můžete založit podnikatelské konto zcela zdarma a rozšířit tak možnosti svého podnikání?\x0aChcete se dozvědět více?"
            ],
            ["Ano", "Připomeň mi to později", "Ne, děkuji", "Proč se mi tento tip ukázal?"]
        )
        
    @staticmethod
    def run_flow():
        wait_for_and_click_entrepreneurCurrentAccountOffer_notification()
        return basic_steps.notification_offer()  

    @staticmethod
    def ok_thanks():
        qabs = basic_steps.run_flow()
        qabs.click(1)           # click to QABS "Ano"

    @staticmethod
    def more_info():
        basic_steps.ok_thanks()
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )  
        qabs.click(2)     # click to QABS "Chci víc podrobností"


@TestSuite
@labels("DoKapsy", "Smart")
@TC_setup(entrepreneurCurrentAccountOffer_test_setup)
class UC0029_entrepreneurCurrentAccountOffer:
    # SC1 later 
    def remind_me_later():
        qabs = basic_steps.run_flow()
        qabs.click(2)      # click to QABS "Připomeň mi to později"
        expecting_utterance(get_remind_me_later_utterance())

    # SC1 no thanks
    def No_thanks():
        wait_for_and_click_entrepreneurCurrentAccountOffer_notification()
        qabs = basic_steps.notification_offer()
        qabs.click(3)      # click to QABS "Ne, děkuji"
        qabs = expecting_utterance(
            Utterance(["Dobře. Když změníte názor, stačí se na mě obrátit."])
            + what_else_can_I_do_utterance
        )

    # SC1 why
    def Why_this():
        wait_for_and_click_entrepreneurCurrentAccountOffer_notification()
        qabs = basic_steps.notification_offer()
        qabs.click(4)       # click to QABS "Proč se mi tento tip ukázal?"
        qabs = expecting_utterance(
            why_this_tip_utterance
            + Utterance(
                ["Víte, že si u nás můžete založit podnikatelské konto zcela zdarma a rozšířit tak možnosti svého podnikání?\nChcete se dozvědět více?"],
                ["Ano", "Připomeň mi to později", "Ne, děkuji", "Proč se mi tento tip ukázal?"]
            )
        )
    
    # SC2 more info
    def more_info():
        basic_steps.more_info()
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        qabs.click(1)       # klikne na QAB "Už vím vše, děkuji"
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        ) 

    # SC2 more info again
    def more_info_again():
        basic_steps.more_info()    
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        qabs.click(1)       # klikne na QAB "Už vím vše, děkuji"
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )
        qabs.click(2)       # klikne na QAB "Chci víc podrobností"
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        qabs.click(1)   # klikne na QAB "Už vím vše, děkuji"
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )                

    # SC2 more info QAAS - Jaké jsou výhody podnikatelského konta?   
    def more_info_QAAS_merits():
        qabs = basic_steps.more_info()
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        click_button(qabsText[0]) # klikne na button "Jaké jsou výhody podnikatelského konta?"
        qabs = expecting(
            [
                "Účet máte zdarma bez jakýchkoli podmínek. V rámci účtu máte také neomezený počet příchozích a odchozích tuzemských plateb. A také bezkontaktní platební kartu Mastercard Business Standard pojištěnou proti ztrátě a krádeži."
            ],
            ["Už vím vše, děkuji", "Ukaž mi nejčastější dotazy"]
        )
        qabs.click(2)       # klikne na QAB "Ukaž mi nejčastější dotazy"
        qabs = expecting(
            [
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )

    # SC2 more info QAAS - Proč si sjednat podnikatelské konto?   
    def more_info_QAAS_why_order_it():
        qabs = basic_steps.more_info()
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        click_button(qabsText[1])     # klikne na button "Proč si sjednat podnikatelské konto?"
        qabs = expecting(
            [
                "Oddělení soukromých a podnikatelských financí je pro vás bezpečnější a přehlednější.\x0aNavíc získáte i další výhody, jako je třeba propojení s platebními terminály ČSOB na 1 rok zcela bez poplatků."
            ],
            ["Už vím vše, děkuji", "Ukaž mi nejčastější dotazy"]
        )
        qabs.click(2)        # klikne na QAB "Ukaž mi nejčastější dotazy"
        qabs = expecting(
            [
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )

    # SC2 more info QAAS - Můžu si konto sjednat on-line?   
    def more_info_QAAS_order_it_online():
        qabs = basic_steps.more_info()
        qabs = expecting(
            [
                "Ráda vám poradím. Co by vás zajímalo?",
                qabsText[0],
                qabsText[1],
                qabsText[2]
            ],
            ["Už vím vše, děkuji"]
        )
        click_button(qabsText[2])     # klikne na button "Můžu si konto sjednat on-line?"
        qabs = expecting(
            [
                "Podnikatelské konto si sjednáte během pěti minut přímo na stránkách podnikatelského konta, třeba i rovnou z mobilu."
            ],
            ["Už vím vše, děkuji", "Ukaž mi nejčastější dotazy"]
        )
        click_and_check_url_and_return(604, 1638, "podnikatelskekonto.csob.cz") # MZL(779, 1709)
        qabs.click(1)       # klikne na QAB "Už vím vše, děkuji"
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )

    # SC3 make deal - Můžu si konto sjednat on-line?
    def make_deal():
        qabs = basic_steps.ok_thanks()
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )
        qabs.click(1)       # klikne na QAB "Ano, mám zájem"
        qabs = expecting(
            [
                "Výborně, váš zájem mě těší. 😎Podnikatelské konto si můžete sjednat on-line do 5 minut."
            ],
            ["Zařídit on-line"]
        )
        qabs.click(1)       # klikne na QAB "Zařídit on-line"
        qabs = expecting_utterance(
            # Utterance([f"To je skvělá volba, {ctx.config.user.first_name}. Nyní klikněte na odkaz podnikatelskekonto.csob.cz, kde aktivaci dokončíte."])
            Utterance([f"To je skvělá volba, Radka. Nyní klikněte na odkaz podnikatelskekonto.csob.cz, kde aktivaci dokončíte."])
            + what_else_can_I_do_utterance
        )
        click_and_check_url_and_return(380, 1483, "podnikatelskekonto.csob.cz")

    # SC2 make deal - Ne, děkuji
    def sc2_no_thanks():
        basic_steps.ok_thanks()
        qabs = expecting(
            [
                "Kromě bezpečného oddělení svých soukromých financí získáte přístup k dalším vychytávkám pro podnikatele.\x0aMůžete mít platební terminál, výhodné úvěry, aplikaci Smart a mnoho dalších.\x0aMáte zájem o nastavení podnikatelského konta?"
            ],
            ["Ano, mám zájem", "Chci víc podrobností", "Ne, děkuji"]
        )
        qabs.click(3)   # klikne na QAB "Ne, děkuji"
        qabs = expecting_utterance(
            Utterance(["Dobře. Když změníte názor, stačí se na mě obrátit."])
            + what_else_can_I_do_utterance
        )
        
