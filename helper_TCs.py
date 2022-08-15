from common import *
from TCs.fdwk_prefs_BtA import BtA_test_case_setup_advanced

@TestSuite
class Helper_TCs:
    # @only_this
    def preference():
        sudo_user_preference()
    
    # @only_this
    @TC_setup(BtA_test_case_setup_advanced)
    def send_all_notifs_as_of_20211112():
        notifs = [
            "sudo kate pošli mi pušku na změnu distribučních kanálů",
            "sudo kate pošli mi pušku na neplnění podmínek nového prémiového účtu",
            "sudo kate pošli mi pušku na neplnění podmínek nového prémiového účtu bez bankéře",
            "sudo kate pošli mi pušku na neplnění podmínek existujícího prémiového účtu",
            "sudo kate pošli mi pušku na neplnění podmínek existujícího prémiového účtu bez bankéře",
            "sudo kate pošli mi pušku na změnu distribučního kanálu",
            "sudo kate pošli mi pušku na změnu distribučních kanálů",
            "sudo kate pošli mi pušku na výročí podnikání",
            "sudo kate pošli mi pušku na nabídku podnikatelského konta",
            "sudo kate pošli mi pušku na expireid",
            "sudo kate pošli mi pušku na nevyužité osobní pojištění",
            "sudo kate pošli mi pušku na automatickou splátku kreditky kvůli nové kartě",
            "sudo kate pošli mi pušku na automatickou splátku kreditky kvůli nezaplacení",
            "sudo kate pošli mi pušku na odeslání karty poštou",
            "sudo kate pošli mi pušku na doručení karty",
            "sudo kate pošli mi pušku na expiraci karty",
        ]

        for n in notifs[:1]:
            sudo_notification(n)

        import os
        os._exit(0)



    # @only_this
    def checklist():
        sudo_notification("sudo kate pošli mi pušku na změnu distribučních kanálů")
        wait_for_and_click_notification("Víte, že přechodem na elektronické výpisy můžete ušetřit stovky korun ročně? 💰\n\nKlepněte pro více informací.")

        qabs = expecting(
            [
                f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.",
                "Zjistila jsem, že si necháváte zasílat výpisy z účtu poštou. Přechodem na elektronickou formu šetříte nejen svou peněženku, ale i lesy. 🏞️",
                "Můžu vám pomoct elektronické výpisy nastavit nebo se vám třeba připomenout později. Co by vám vyhovovalo?"
            ],
            ["Chci elektronické výpisy", "Připomeň mi to později", "Nechci elektronické výpisy", "Proč se mi tento tip ukázal?"]
        )

        qabs.click(1)

        expecting([
            "Elektronické výpisy můžete mít každý měsíc v internetovém bankovnictví ve formě PDF a nic za ně neplatíte.",
            "U kterých účtů chcete přejít na elektronické výpisy?",
            "0500021502/0800 - běžný",
            "1207098544 - spořicí",
            "41-0850010744/0303 - termínovaný",
            "Potvrdit výběr",
        ])

        click_checkbox("1207098544 - spořicí")
        click_button("Potvrdit výběr")

        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()
        get_kate_reply_now()

    # @only_this
    def testing_reporting_when_All_I_Have_Is_General_Error():
        expecting(["Došlo k obecné chybě. Prosím zkuste to znovu později."])

    # @only_this
    def uc64():
        activation_Y2k_text: list[str] = [
            "Nechci papírové výpisy",
            "Nechci dostávat papírové výpisy",
            "Chci elektronické výpisy",
            "Chci změnit formát výpisů",
            "Jde změnit papírový výpis na elektronický výpis?",
            "Můžeš mi změnit papírový výpis na elektronický výpis?"
        ]

        for ph in activation_Y2k_text:
            send_answer(ph)
            wait_for_element_by_id("chatfragment_quickreply_rcv", throw_ex = False)
            pass
    
    def first_fallback():
        for i in range(6):
            send_answer(f"Spouštění CASE81 - průchod")
        
            expecting(
                [{ # options
                    # csobkate-4940: s komentami
                    # a asi tiez csobkate-6083
                    "Omlouvám se, teď jsem dobře nerozuměla. Ještě jednou, prosím.",
                    "Pardon. Co říkáte?",
                    "Nerozuměla jsem. Co to bylo?"
                }],
                ["Co všechno umíš?"]
            )
            ctx.test_case_teardown()
            ctx.test_case_setup()
