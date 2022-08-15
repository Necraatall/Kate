# from TCs.fdwk_prefs_BtA import test_case_user_setup
# from common import *

# def sudo_card_unblocking_notification_mock():
#     sudo_notification("sudo kate pošli mi pušku na odblokovaní karty")

# def wait_for_and_click_card_unblocking_notification_mock():
#     wait_for_and_click_notification("Máte zablokovanou kartu! Částka 999.90 CZK neodešla z vašeho účtu. Chcete poradit jak ji odblokovat? 🧐")

# def card_unblocking_test_setup():
#     test_case_user_setup(UserType.advanced)
#     sudo_card_unblocking_notification_mock()

# # sudo kate pošli mi pušku na odblokovaní karty
# # sudo kate pošli mi pušku na odblokovaní karty ostrý dialog
# # sudo kate pošli mi pušku na odblokovaní karty klient ostrý dialog zakaznik nemá prava

# text_after_notification = ["Zadejte KateId a CardId ve formatu: !unblocking_card;1234567890123;1111222233334444!"]

# answer_notify_card = ["!unblocking_card;1234567890123;1111222233334444!"]

# class basic_steps:
#     @staticmethod
#     def notification_offer():
#         wait_for_one_of_texts(text_after_notification)
#         return expecting(f"{get_current_day_greeting()}, {ctx.config.user.first_name}, tady Kate.", text_after_notification)

# # dodat do spoustece       
#         #send_answer(answer_notify_card)

#     @staticmethod
#     def run_flow_one():
#         #report_label("CaseID 0064")
#         wait_for_and_click_card_unblocking_notification_mock()
#         return basic_steps.notification_offer() 

# @TestSuite
# @labels("DoKapsy", "Smart")
# @TC_setup(card_unblocking_test_setup)
# #@only_this
# class UC0058_Y2K_card_unblocking_one_mock:
#     # SC1 later 
#    # def remind_me_later():
#    qabs = basic_steps.run_flow_one()
#    send_answer(answer_notify_card)