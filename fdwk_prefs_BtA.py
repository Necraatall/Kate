from selenium.common.exceptions import StaleElementReferenceException

import random
from common import *



def get_text_to_user_types() -> dict[str, UserType]:
    return {
        f"{ctx.config.user.first_name}, v této chvíli jsem plnohodnotná Kate a mohu vám zasílat chytré tipy a poskytovat služby třetích stran. Díky tomu vás mohu třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.":
            UserType.advanced,
        f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.":
            UserType.basic,
        Steps.get_fdwk_2_2_first_Kate_reply_utt().texts[0]:
            UserType.init,
        f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate. 👋":  # csobkate-5031
            UserType.non_init,
        f"{get_current_day_greeting()}, {ctx.config.user.first_name}. 👋":
            UserType.non_init,
        f"Zdravím, {ctx.config.user.first_name}, tady Kate. 👋":
            UserType.non_init,
        f"Zdravím, {ctx.config.user.first_name}. 👋":
            UserType.non_init,
    }

def get_text_to_user_type(key: str) -> UserType:
    return get_text_to_user_types()[key]

def pref_test_case_setup(expected_user_type: UserType, reenter: bool = True):
    ctx.test_case_settings_setup()
    
    found = wait_for_one_of_texts(get_text_to_user_types().keys())
    ctx.user_type = get_text_to_user_type(found)

    if (expected_user_type == ctx.user_type):
        return
    elif (ctx.user_type == UserType.basic                        and expected_user_type == UserType.advanced): preferences_basic_yes_core_conversation()
    elif (ctx.user_type == UserType.advanced                     and expected_user_type == UserType.basic)   : preferences_advanced_no_core_conversation()
    elif (ctx.user_type == UserType.init                         and expected_user_type == UserType.basic)   : Fdwk_2_2.no()
    elif (ctx.user_type == UserType.init                         and expected_user_type == UserType.advanced): Fdwk_2_2.yes_yes()
    elif (ctx.user_type in { UserType.basic, UserType.advanced } and expected_user_type == UserType.init)    : sudo_reset_user()
    else:
        raise Exception(
            f"Unexpected state. Should be covered by elifs. (user_type = {ctx.user_type}, expected_user_type = {expected_user_type})")

    if reenter:
        ctx.test_case_teardown()
        pref_test_case_setup(expected_user_type)

def pref_test_case_setup_advanced(): pref_test_case_setup(UserType.advanced)
def pref_test_case_setup_basic()   : pref_test_case_setup(UserType.basic)
def pref_test_case_setup_init()    : pref_test_case_setup(UserType.init)

def BtA_test_case_setup(expected_user_type: UserType):
    pref_test_case_setup(expected_user_type)
    ctx.test_case_teardown()
    ctx.test_case_setup()

def BtA_test_case_setup_advanced(): BtA_test_case_setup(UserType.advanced) # @todo: should be renamed to kate_test_case_setup_advanced or something
def BtA_test_case_setup_basic()   : BtA_test_case_setup(UserType.basic)
def BtA_test_case_setup_init()    : BtA_test_case_setup(UserType.init)

def fdwk_test_case_setup():
    ctx.test_case_setup()
    
    for try_i in range(10):
        try:
            found = wait_for_one_of_texts(get_text_to_user_types().keys())
        except StaleElementReferenceException:
            continue
        break
    ctx.user_type = get_text_to_user_type(found)

    if (ctx.user_type == UserType.init): return
    elif (ctx.user_type == UserType.non_init): sudo_reset_user()
    else:
        raise Exception(
            f"Unexpected state. Should be covered by elifs. (user_type = {ctx.user_type})")
    
    ctx.test_case_teardown()
    fdwk_test_case_setup()

def test_case_user_setup(expected_user_type: UserType):
    if (expected_user_type == UserType.any):
        raise Exception("Why do you want unknown user type?") # Use test_case_setup() if It actually make sense.
    elif (expected_user_type == ctx.user_type):
        ctx.test_case_setup() # nop
    elif (expected_user_type == UserType.non_init and (UserType.non_init.__contains__(ctx.user_type))):
        ctx.test_case_setup()  # nop
    elif (expected_user_type == UserType.init):
        fdwk_test_case_setup()
        # Fdwk_2_2.maybe_later()
    elif (expected_user_type == UserType.basic):
        if (ctx.user_type == UserType.init):
            ctx.test_case_setup()
            Fdwk_2_2.no()
            ctx.test_case_teardown()
            ctx.test_case_setup()
        else:
            pref_test_case_setup(UserType.basic, reenter= False)
            ctx.test_case_teardown()
            ctx.test_case_setup()
    elif (expected_user_type == UserType.advanced):
        if (ctx.user_type == UserType.init):
            ctx.test_case_setup()
            Fdwk_2_2.yes_yes()
            ctx.test_case_teardown()
            ctx.test_case_setup()
        else:
            pref_test_case_setup(UserType.advanced, reenter= False)
            ctx.test_case_teardown()
            ctx.test_case_setup()
    elif (expected_user_type == UserType.non_init and ctx.user_type in { UserType.init, UserType.any}):
        ctx.test_case_setup()
        if ctx.user_type == UserType.any:
            found = wait_for_one_of_texts(get_text_to_user_types().keys())
            ctx.user_type = get_text_to_user_type(found)
        if ctx.user_type == UserType.init:
            random.choice([Fdwk_2_2.yes_yes(), Fdwk_2_2.no()])()
    else:
        raise Exception(
            f"Unexpected state. Should be covered by elifs. (user_type = {ctx.user_type}, expected_user_type = {expected_user_type})")


def get_contract_text():
    if   ctx.config.user.gender == config.Gender.male: # csobkate-1333
        seznamil_a = "seznámil"
    elif ctx.config.user.gender == config.Gender.female:
        seznamil_a = "seznámila"
        
    if   ctx.config.app_type == config.AppType.DoKapsy:
        return f"Stisknutím tlačítka „Souhlasím“, příp. jiným souhlasným projevem vůle v rámci komunikace s Kate, uzavírám smlouvu o využívání Kate se společnostmi Československá obchodní banka, a.\xa0s., IČO: 00001350; ČSOB Pojišťovna, a. s., člen holdingu ČSOB, IČO 45534306, a Ušetřeno.cz s.r.o., IČO 24684295, jejímž obsahem jsou Podmínky používání aplikace DoKapsy od ČSOB, se kterými jsem se {seznamil_a} a které jako součást smlouvy přijímám. Rovněž tímto potvrzuji seznámení se s\xa0informacemi o zpracování osobních údajů."
    elif ctx.config.app_type == config.AppType.Smart:
        return f"Stisknutím tlačítka „Souhlasím“, příp. jiným souhlasným projevem vůle v rámci komunikace s Kate, uzavírám smlouvu o využívání Kate se společnostmi Československá obchodní banka, a.\xa0s., IČO: 00001350; ČSOB Pojišťovna, a. s., člen holdingu ČSOB, IČO 45534306, a Ušetřeno.cz s.r.o., IČO 24684295, jejímž obsahem jsou Obchodní podmínky pro ČSOB Identitu, se kterými jsem se {seznamil_a} a které jako součást smlouvy přijímám. Rovněž tímto potvrzuji seznámení se s\xa0informacemi o zpracování osobních údajů."
    else:
        raise NotImplementedError()

def preferences_advanced_no_core_conversation():
    qabs = expecting(
        [
            f"{ctx.config.user.first_name}, v této chvíli jsem plnohodnotná Kate a mohu vám zasílat chytré tipy a poskytovat služby třetích stran. Díky tomu vás mohu třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
            "Chcete současné nastavení zachovat?"
        ],
        ["Ano", "Ne, děkuji"]
    )
    qabs.click(2) # Ne

    expecting(
        [
            "Dobře, rozumím. Přepínám se na \"Mini Kate\" a mohu vám odpovídat jen na obecné otázky. Posílat užitečné tipy mám od vás zakázáno.",
            "Mohu pro vás udělat ještě něco dalšího?"
        ],
        ["Co všechno umíš?"]
    )
    ctx.user_type = UserType.basic

def preferences_basic_yes_core_conversation():
    qabs = expecting(
        [
            f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
            "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
            "Uděláte ze mne plnohodnotnou chytrou Kate?"
        ],
        ["Ano", "Chci vědět víc", "Ne, děkuji"]
    )
    qabs.click(1)

    qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
    qabs.click(1) # yes

    qabs = expecting(
        [
            "Výborně, přepínám se na plnohodnotnou Kate a mohu se vám ozývat s užitečnými tipy. 😊",
            "Pojďme se podívat, co pro vás mohu udělat."
        ],
        ["Co všechno umíš?"]
    )
    ctx.user_type = UserType.advanced


@TestSuite
@labels("DoKapsy", "Smart", "user_types")
class ManagePreferences:
    @ordered
    @TC_setup(pref_test_case_setup_advanced)
    def preferences_advanced_yes():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem plnohodnotná Kate a mohu vám zasílat chytré tipy a poskytovat služby třetích stran. Díky tomu vás mohu třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Chcete současné nastavení zachovat?"
            ],
            ["Ano", "Ne, děkuji"]
        )
        qabs.click(1)  # Ano

        expecting(
            [
                "Výborně, zůstávám plnohodnotnou Kate! Budu pro vás i nadále hledat užitečné tipy. 😊",
                "Pojďme se podívat, co pro vás mohu udělat."
            ],
            ["Co všechno umíš?"]
        )

    @ordered
    @TC_setup(pref_test_case_setup_advanced)
    def preferences_advanced_no():
        preferences_advanced_no_core_conversation()

    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_no():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
                "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Uděláte ze mne plnohodnotnou chytrou Kate?"
            ],
            ["Ano", "Chci vědět víc", "Ne, děkuji"]
        )
        qabs.click(3) # no

        qabs = expecting(
            [
                "Dobře, rozumím a zůstávám \"Mini Kate\"",
                "Pojďme se podívat, co pro vás mohu udělat."
            ],
            ["Co všechno umíš?"]
        )

    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_yes_no():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
                "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Uděláte ze mne plnohodnotnou chytrou Kate?"
            ],
            ["Ano", "Chci vědět víc", "Ne, děkuji"]
        )
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
        qabs.click(3) # no

        qabs = expecting(
            [
                "Dobře, rozumím a zůstávám \"Mini Kate\"",
                "Pojďme se podívat, co pro vás mohu udělat."
            ],
            ["Co všechno umíš?"]
        )
    
    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_more_no():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
                "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Uděláte ze mne plnohodnotnou chytrou Kate?"
            ],
            ["Ano", "Chci vědět víc", "Ne, děkuji"]
        )
        qabs.click(2)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(2)

        expecting(
            [
                "Dobře, rozumím a zůstávám \"Mini Kate\"",
                "Pojďme se podívat, co pro vás mohu udělat."
            ],
            ["Co všechno umíš?"]
        )

    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_more_yes():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
                "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Uděláte ze mne plnohodnotnou chytrou Kate?"
            ],
            ["Ano", "Chci vědět víc", "Ne, děkuji"]
        )
        qabs.click(2)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(1)

        Steps.fdwk_2_2_contract_reply(seen_how_it_works = True)

    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_yes_more_yes():
        qabs = expecting(
            [
                f"{ctx.config.user.first_name}, v této chvíli jsem jen taková „Mini Kate“ a mohu vám odpovídat jen na obecné otázky. Užitečné tipy nemáte povolené.",
                "Když si ale aktivujete moji plnou verzi, budu vás moci třeba upozornit na končící platnost karty a ověřit, kam máme poslat novou.",
                "Uděláte ze mne plnohodnotnou chytrou Kate?"
            ],
            ["Ano", "Chci vědět víc", "Ne, děkuji"]
        )
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
        qabs.click(2) # chci vedet vic

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(1)

        Steps.fdwk_2_2_contract_reply(seen_how_it_works = True)

    @ordered
    @TC_setup(pref_test_case_setup_basic)
    def preferences_basic_yes_yes():
        preferences_basic_yes_core_conversation()

    @ordered
    @TC_setup(pref_test_case_setup_init)
    def preferences_init():
        Steps.fdwk_2_2_first_Kate_reply()


@TestSuite
@TC_setup(fdwk_test_case_setup)
@labels("DoKapsy", "Smart", "user_types")
class Fdwk_2_2:
    @ordered
    def yes__how_it_works__yes():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
        qabs.click(2)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(1)

        Steps.fdwk_2_2_contract_reply(seen_how_it_works = True)

    @ordered
    def maybe_later():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(2) # mozna pozdeji

        expecting_utterance(
            Utterance(["Dobře, pobavíme se o tom příště."])
            + what_Kate_can_do_utt
        )

        ctx.driver.swipe(200, 600, 200, 200, 1000) # TODO: BTA testy by mali byt viac explicitne; user setup by mal robit menej. Potom nemusim resetovat scrolling

    def yes_yes():
        Steps.fdwk_2_2_yes_yes_main()

    def yes_no():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
        qabs.click(3)

        ctx.user_type = UserType.basic
        expecting_utterance(
            Utterance([
                "Rozumím. Nebudu vám své tipy posílat.",
                "Pokud o ně budete mít v budoucnu zájem, v nastavení mě přepněte do plné verze."
            ])
            + what_Kate_can_do_utt
        )

    def no():
        Steps.fdwk_2_2_no_main()

    def how_it_works__no():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(3)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(2)

        expecting_utterance(
            Utterance([
                "Rozumím. Nebudu vám své tipy posílat.",
                "Pokud o ně budete mít v budoucnu zájem, v nastavení mě přepněte do plné verze."
            ])
            + what_Kate_can_do_utt
        )

    def how_it_works__yes__no():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(3)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = True)
        qabs.click(2)

        ctx.user_type = UserType.basic
        expecting_utterance(
            Utterance([
                "Rozumím. Nebudu vám své tipy posílat.",
                "Pokud o ně budete mít v budoucnu zájem, v nastavení mě přepněte do plné verze."
            ])
            + what_Kate_can_do_utt
        )

    def how_it_works__yes__yes():
        qabs = Steps.fdwk_2_2_first_Kate_reply()
        qabs.click(3)

        qabs = expecting(
            [
                "Mojí hlavní předností je, že vás znám. Přeci jen už jsem v bance nějaký ten pátek. 😎\n\nDokážu vás vhodně upozornit - třeba na rozpracovanou hypotéku. Umím vám také nahlásit, že vám vyprší občanka nebo že nečerpáte bezplatné výhody svého účtu.",
                "Užitečné tipy vybírám podle vaší aktuální situace, historie plateb a nastavení vašich produktů.",
                "Máte o mé užitečné tipy zájem?"
            ],
            ["Ano, pojďme na to", "Ne, děkuji"]
        )
        qabs.click(1)

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = True)
        qabs.click(1)

        ctx.user_type = UserType.advanced
        expecting_utterance(
            Utterance(["Výborně! Jakmile najdu něco zajímavého, dám vám vědět."])
            + what_Kate_can_do_utt
        )


@TestSuite
@labels("DoKapsy", "Smart", "user_types")
class BasicToAdvanced:
    # 2021-08-05:
    # advanced case: Chci levnější energii
    # basic case: Pojištění domácích mazlíčků
    @user_type(UserType.advanced)
    @ordered
    def BtA_advanced_user__advanced_case():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        expecting(
            [
                "Se změnou dodavatele energií vám nejlépe poradí v Ušetřeno.cz.",
                [
                    "Mohu vás spojit s mými kolegy, nebo se připomenout později. Co vy na to?",
                    "Co kdyby vám kolegové z Ušetřeno.cz zavolali a probrali s vámi podrobnosti?"
                ]
            ],
            ["Ano, mám zájem", "Ne, děkuji"]
        )

    @user_type(UserType.advanced)
    @ordered
    def BtA_advanced_user__basic_case():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )    
        send_answer("Pojištění domácích mazlíčků")

        expecting(
            ["Víte, že až 90 % vašich výdajů za platby u veterináře by mohlo pokrýt pojištění domácích mazlíčků? Chcete více informací?"],
            ["Ano", "Ne, děkuji"]
        )

    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__basic_case():
        BasicToAdvanced.BtA_advanced_user__basic_case()

    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__no():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_no()

        assert_preference(UserType.basic)

    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__yes_no():
        expecting_utterance(
            get_common_kate_greeting_utt()
            +what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_yes_no()

        assert_preference(UserType.basic)
    
    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__more_no():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_more_no()

        assert_preference(UserType.basic)
    
    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__more_yes():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_more_yes()

        assert_preference(UserType.basic)
    
    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__yes_more_yes():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_yes_more_yes()

        assert_preference(UserType.basic)
    
    @user_type(UserType.basic)
    @ordered
    def BtA_basic_user__advanced_case__yes_yes():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        ManagePreferences.preferences_basic_yes_yes()

        assert_preference(UserType.advanced)

    @user_type(UserType.init)
    @ordered
    def BtA_init_user__basic_case():
        Fdwk_2_2.maybe_later()

        expecting_utterance(
            Utterance(["Dobře, pobavíme se o tom příště."])
            + what_Kate_can_do_utt
        )
        send_answer("Pojištění domácích mazlíčků")

        expecting(
            ["Víte, že až 90 % vašich výdajů za platby u veterináře by mohlo pokrýt pojištění domácích mazlíčků? Chcete více informací?"],
            ["Ano", "Ne, děkuji"]
        )

        assert_preference(UserType.init)

    @user_type(UserType.init)
    @ordered
    def BtA_init_user__advanced_case__no():
        Fdwk_2_2.maybe_later()

        expecting_utterance(
            Utterance(["Dobře, pobavíme se o tom příště."])
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        Steps.fdwk_2_2_no_main(drop_greeting = True)

        assert_preference(UserType.basic)

    @user_type(UserType.init)
    @ordered
    def BtA_init_user__advanced_case__yes_yes():
        Fdwk_2_2.maybe_later()

        expecting_utterance(
            Utterance(["Dobře, pobavíme se o tom příště."])
            + what_Kate_can_do_utt
        )
        send_answer("Chci levnější energii")

        Steps.fdwk_2_2_yes_yes_main(drop_greeting = True)

        assert_preference(UserType.advanced)

import config

class Steps:
    @staticmethod
    def get_fdwk_2_2_first_Kate_reply_utt() -> Utterance:
        return Utterance(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, ráda vás poznávám. Jmenuji se Kate a jsem vaše digitální asistentka.\n\nJsem navržená tak, abych vám poskytla to, co právě potřebujete, v ten správný čas. 💁‍♀️",
                "Umím vám dávat užitečné tipy - třeba na to, že vám vyprší platnost karty nebo že jsem našla prostor, jak můžete ušetřit.\n\nChcete si to vyzkoušet?"
            ],
            ["Ano, pojďme na to", "Možná později", "Chci vědět víc", "Nemám zájem"]
        )
    @staticmethod
    def fdwk_2_2_first_Kate_reply():
        return expecting_utterance(Steps.get_fdwk_2_2_first_Kate_reply_utt())

    @staticmethod
    def fdwk_2_2_contract_reply(seen_how_it_works: bool):
        expected_qabs = ["Souhlasím", "Chci vědět víc", "Ne, děkuji"]
        if seen_how_it_works: # or (seen_how_it_works is None):
            expected_qabs.remove("Chci vědět víc")

        return expecting(
            [
                "Super, jediné, co od vás potřebuji, je souhlas, že vám mohu své tipy posílat.\n\nV nastavení aplikace mě můžete vždycky přepnout do základní verze a já vám nepošlu nic, o co si výslovně neřeknete.",
                get_contract_text()
            ],
            expected_qabs,
        )

    @staticmethod
    def fdwk_2_2_no_main(drop_greeting: bool = False):
        expected_utt = Steps.get_fdwk_2_2_first_Kate_reply_utt()
        if drop_greeting:
            expected_utt.texts.pop(0)
        
        qabs = expecting_utterance(expected_utt)
        qabs.click(4) # nemam zajem

        ctx.user_type = UserType.basic
        # sleep_in_s(3)
        expecting_utterance(
            Utterance([
                "Rozumím. Nebudu vám své tipy posílat.",
                "Pokud o ně budete mít v budoucnu zájem, v nastavení mě přepněte do plné verze."
            ])
            + what_Kate_can_do_utt
        )

    @staticmethod
    def fdwk_2_2_yes_yes_main(drop_greeting: bool = False):
        expected_utt = Steps.get_fdwk_2_2_first_Kate_reply_utt()
        if drop_greeting:
            expected_utt.texts.pop(0)
        
        qabs = expecting_utterance(expected_utt)
        qabs.click(1) # Ano, pojďme na to

        qabs = Steps.fdwk_2_2_contract_reply(seen_how_it_works = False)
        # TODO: links
        qabs.click(1)

        ctx.user_type = UserType.advanced
        expecting_utterance(
            Utterance(["Výborně! Jakmile najdu něco zajímavého, dám vám vědět."])
            + what_Kate_can_do_utt
        )