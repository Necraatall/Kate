from TCs.fdwk_prefs_BtA import test_case_user_setup
from common import *

def sudo_entrepreneurshipFoundationCongratulation_notification():
    sudo_notification("sudo kate pošli mi pušku na výročí podnikání")

def wait_for_and_click_entrepreneurshipFoundationCongratulation_notification():
    wait_for_and_click_notification("Všimla jsem si, že máte dnes 1. výročí založení vašeho podnikání. Víte, že pro vás mám malou pozornost? 🤗")

def entrepreneurshipFoundationCongratulation_test_setup():
    test_case_user_setup(UserType.advanced)
    sudo_entrepreneurshipFoundationCongratulation_notification()

# toto je gratulace
text_gratulation = "Do dalších úspěšných let by vám mohl být nápomocný náš portál \"Průvodce podnikáním\" s aktuálními tipy jak na to, mimo jiné i z oblasti daní.\x0a\x0aZajímat by vás mohl i náš inspirativní newsletter, který rozesíláme několikrát do roka. 🧐"

# toto je osloveni a zakladni hlaska     
def get_text_greetings_gratulation():
    return [                
        f"{get_current_day_greeting()}" + ", " + f"{ctx.config.user.first_name}" + ", tady Kate.",
        "Gratuluji vám k 1. výročí založení vašeho podnikání. Máme pro vás zajímavý tip, co vy na to? 🤝",
        text_gratulation
    ]

# toto je odpoved na why_this
text_because = [
        "Jsem tu od toho, abych vám mimo jiné pomohla v různých situacích a případně i něco \"ušetřila\". 🙂 Proto ode mne občas uvidíte podobné, věřím, že užitečné, tipy. \x0a\x0aPokud je nechcete dostávat, můžete je jednoduše vypnout v nastavení aplikace.",
        text_gratulation
    ]
link_help_company = "pruvodcepodnikanim.cz"

# toto jsou zakladni tlacitka qabs k uvodni hlasce
qabs_start = ["OK, děkuji", "Proč se mi tento tip ukázal?"]

@TestSuite
@labels("DoKapsy", "Smart")
@TC_setup(entrepreneurshipFoundationCongratulation_test_setup)
class UC0035_entrepreneurshipFoundationCongratulation:
    def ok_thanks():
        wait_for_and_click_entrepreneurshipFoundationCongratulation_notification()
        qabs = expecting(
            get_text_greetings_gratulation(),
            qabs_start
        )
        click_and_check_url_and_return(543, 1302, link_help_company)
        qabs.click(1)   # click on qabs "OK, děkuji"
        qabs = expecting_utterance(what_else_can_I_do_utterance)

    def Why_this():
        wait_for_and_click_entrepreneurshipFoundationCongratulation_notification()
        qabs = expecting(
            get_text_greetings_gratulation(),
            qabs_start
        )
        click_and_check_url_and_return(543, 1302, link_help_company)
        qabs.click(2)   # click on qabs "Proč se mi tento tip ukázal?"
        qabs = expecting(
            text_because,
            qabs_start
        )
        click_and_check_url_and_return(543, 1302, link_help_company)
        qabs.click(2)   # click on qabs "Proč se mi tento tip ukázal?"
        qabs = expecting(
            text_because,
            qabs_start
        )
        click_and_check_url_and_return(543, 1302, link_help_company)
        qabs.click(1)   # click on qabs "OK, děkuji"
        qabs = expecting_utterance(what_else_can_I_do_utterance)
