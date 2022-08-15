from appium.webdriver.extensions.android.nativekey import AndroidKey
from TCs.fdwk_prefs_BtA import test_case_user_setup
from common import *
import random


def cardLimitChange_test_setup():
    test_case_user_setup(UserType.advanced)


# toto jsou otazky pro Kate
chatbox_text_card_questions = [
        "Jaky je muj limit pro platbu kartou.",
        "Chci si snížit limit na kartě.",
        "Jaký mám limit na kartě?",
        #"Chtela bych zvednout limit platebni karty", # TO DO je tam BUG Nechyta se - TO Miro Marek
        "Co mám dělat při přečerpaném limitu?",
        "Hledám limity výběru.",
        "Jak si můžu zvýšit týdenní limit pro výběry?",
        "Jak si změním denní limit?",
        "Jak změnit limit na kartě?",
        "Jak změním limit ke kartě?",
        "Jak změním limity na kartě?",
        "limity karet",
        "Jak zvýšit týdenní limit výběru z bankomatu?",
        "Jak zvýším limit pro platební kartu?",
        "Kde najdu informaci o limitu vyberu?",
        "Kde najdu limit pro výběry?",
        "Kde se dozvim, jaky mam limit pro vyber kartou v bankomatu?",
        "Kde si můžu zvýšit limit pro výběr z bankomatu?",
        "Kde zjistím denní limit pro platby kartou?",
        "Kolik je limit na mojí platební kartě?",
        "Lze zvýšit limit na kartu bez docházení na pobočku?",
        "Můžu si zvýšit limit pro výběr z bankomatu?",
        "Nevím, kde zkontrolovat limity ke své kartě.",
        "V jake sekci najdu limit pro tydenni vyber kartou?",
        "Kde najdu jaký je můj limit na kartě?",
        "potřebovala bych navýšit limit u karty"
    ]

@TestSuite
# @labels("DoKapsy")
@TC_setup(cardLimitChange_test_setup)
class UC0060_cardLimitChange:
    # different questions lead to different position of links, so test to click on them needs same question everytime.
    def links():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )

        send_answer(chatbox_text_card_questions[0])

        expecting_utterance(
            Utterance([
                "Limity pro převod v internetovém bankovnictví nebo Smartu si zjistíte i případně upravíte ve svém internetovém bankovnictví v \"Menu\" > \"Nastavení\" > \"Přehled limitů\".",
                "Nastavení svých karet (limity, platby přes internet, zobrazení PIN, dočasná blokace) si upravíte v internetovém bankovnictví nebo ve Smartu hned na první obrazovce: \"Můj přehled\" > \"Platební karty\"."
            ])
            + what_else_can_I_do_utterance
        )

        # click_and_check_url_and_return(558, 1370, "csob.cz/portal/jaknato/internetove-bankovnictvi") # mlz(527, 1428)
        click_and_check_url_and_return(527, 1428, "csob.cz") # mlz(527, 1428) mku (507, 1370, "csob.cz")

        ctx.driver.tap([(783, 1549)]) # mlz(783, 1549) mku (550, 1533)
        Smart_login()
        wait_for_element_by_text("Platební karty")

        
        ctx.driver.press_keycode(AndroidKey().BACK)
        wait_for_element_by_id(chat_root_id) # bug: csobkate-4760


    # this test is for smoke tests
    def random_card_question():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )

        chosen_question = random.choice(chatbox_text_card_questions)
        send_answer(chosen_question)

        expecting_utterance(
            Utterance([
                "Limity pro převod v internetovém bankovnictví nebo Smartu si zjistíte i případně upravíte ve svém internetovém bankovnictví v \"Menu\" > \"Nastavení\" > \"Přehled limitů\".",
                "Nastavení svých karet (limity, platby přes internet, zobrazení PIN, dočasná blokace) si upravíte v internetovém bankovnictví nebo ve Smartu hned na první obrazovce: \"Můj přehled\" > \"Platební karty\"."
            ])
            + what_else_can_I_do_utterance
        )

    # this test is for thorough testing
    @skip
    def all_card_questions():
        expecting_utterance(
            get_common_kate_greeting_utt()
            + what_Kate_can_do_utt
        )

        for q in chatbox_text_card_questions:
            send_answer(q)

            expecting_utterance(
                Utterance([
                    "Limity pro převod v internetovém bankovnictví nebo Smartu si zjistíte i případně upravíte ve svém internetovém bankovnictví v \"Menu\" > \"Nastavení\" > \"Přehled limitů\".",
                    "Nastavení svých karet (limity, platby přes internet, zobrazení PIN, dočasná blokace) si upravíte v internetovém bankovnictví nebo ve Smartu hned na první obrazovce: \"Můj přehled\" > \"Platební karty\"."
                ])
                + what_else_can_I_do_utterance
            )
