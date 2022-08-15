from appium.webdriver.extensions.android.nativekey import AndroidKey

from TCs.fdwk_prefs_BtA import test_case_user_setup
from common import *


#CEBM rand from len range = 0 to array

text_answer_send_complaint = [	
    "Pokud něco není v pořádku, neotálejte a\xa0dejte prosím\xa0vědět kolegům na reklamacích. Vynasnažíme se situaci napravit.",
    "Kontaktovat je můžete  e-mailem nebo telefonicky +420 800 150 150.", # dve mezery pred emailem je zatim nereportovana chyba
    "Všechny způsoby, jak se s námi v této věci spojit, naleznete na webu ČSOB."
    ]

qabs_done = ["Vyřešeno, děkuji"]

link_help_company = "pruvodcepodnikanim.cz"

text_where_to_find_payment_confirmations = str("Potvrzení o provedení platby si můžete stáhnout v aplikaci CEB Mobile v Detailu účtu nebo ve službě ČSOB CEB v menu \"Účty\" > \"Pohyby na účtu\".")

text_where_to_save_bank_conection = [
    "Bankovní spojení ve službě ČSOB CEB můžete uložit nebo spravovat hned dvěma způsoby. V menu \"Platby\" > \"Vzory a spojení\" > \"Bankovní spojení\" nebo na formulářích platebních příkazů zvolte Uložit bankovní spojení.",
    "V aplikaci CEB Mobile zvolte obrazovku Bankovní spojení."]

	
text_how_to_find_my_PIN = [
"Informace ke své platební kartě najdete v aplikaci CEB Mobile v záložce Karty nebo ve službě ČSOB CEB v menu \"Karty\" > \"Přehled karet\". ",
"Zde můžete povolit/zakázat platby kartou na internetu (3D Secure).",
"Pokud zde kartu nevidíte, kontaktujte Helpdesk na čísle 495 800 111."]


@TestSuite
@labels("CebM")
class Y2K_K4B_Knowledge_Base:
    def where_to_send_complaint():
        expecting_utterance(get_CebM_kate_intro())
        send_answer("kam odeslat formulář o reklamaci")
        qabs = expecting(text_answer_send_complaint, qabs_done)
        # info
        # gmail testovaciuserkate@gmail.com pass Kate123456789
        # mail link coordinates 971, 1313
        # click_and_check_gmail ends-with ... com.google.android.gm:id/to, like url
        click_and_check_email_address_and_return(971, 1313, "reklamace@csob.cz")    #mzl 971, 1313
        click_and_check_phone_number_and_return(890, 1377, "+420 800 150 150")  #mzl 890, 1377
        click_and_check_url_and_return(1017, 1716, "csob.cz")   #mzl 1017, 1716
        qabs.click(1)            # click to QABS "Vyřešeno, děkuji"
        qabs = expecting_utterance(what_else_can_I_do_utterance)
    
    # @skip
    # TODO pridany funkce a buttony nutny update MZL 8.10.2021
    def where_to_find_payment_confirmation():
        expecting_utterance(get_CebM_kate_intro())
        send_answer("Kde můžu najít potvrzení o platbě?")
        sleep_in_s(5)
        expecting([text_where_to_find_payment_confirmations], ["Co všechno umíš?"])
        ctx.driver.tap([(599, 1647)])       # mzl(599, 1647)
        wait_for_element_by_text("ZOBRAZIT CELOU HISTORII")
        wait_for_element_by_id("action_kate")
        wait_for_element_by_id("action_kate").waiting_click()

    def where_to_save_bank_conection():
        expecting_utterance(get_CebM_kate_intro())    
        send_answer("Chci uložit bankovní spojení")
        expecting(text_where_to_save_bank_conection, ["Co všechno umíš?"])
        ctx.driver.tap([(708, 1762)])       # mzl(708, 1762)
        wait_for_element_by_text("VYTVOŘIT NOVÉ")
        ctx.driver.press_keycode(AndroidKey().BACK)
        wait_for_element_by_id(chat_root_id)

    def how_to_make_payment():
        expecting_utterance(get_CebM_kate_intro())

        send_answer("Jak zadám platbu?")

        expecting(
            ["Platbu zadáte jednoduše v aplikaci CEB Mobile v Platebním příkazu nebo ve službě ČSOB CEB."],
            ["Co všechno umíš?"]
        )

        ctx.driver.tap([(783, 1714)])       # mzl(783, 1714)
        wait_for_element_by_text("VYBRAT")
        ctx.driver.press_keycode(AndroidKey().BACK)
        
        wait_for_element_by_id(chat_root_id)

    def how_to_find_my_PIN():
        expecting_utterance(get_CebM_kate_intro())

        send_answer("Jak si zobrazím PIN?")

        expecting(
            [
                "Informace ke své platební kartě najdete v aplikaci CEB Mobile v záložce Karty nebo ve službě ČSOB CEB v menu \"Karty\" > \"Přehled karet\". ",
                "Zde můžete povolit/zakázat platby kartou na internetu (3D Secure).",
                "Pokud zde kartu nevidíte, kontaktujte Helpdesk na čísle 495 800 111."
            ],
            ["Co všechno umíš?"]
        )

        click_and_check_phone_number_and_return(285, 1771, "+420 495 800 111")        #mzl 285, 1771
