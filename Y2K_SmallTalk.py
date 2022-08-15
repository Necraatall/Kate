from appium.webdriver.extensions.android.common import Common
from TCs.intents_for_smalltalk import *
import random
import calendar
import datetime
from datetime import date
from time import gmtime, strftime

class start_steps:
    @staticmethod
    def run_flow():

        if ctx.config.app_type == AppType.DoKapsy:
            expecting_utterance(
                get_common_kate_greeting_utt()
                + what_Kate_can_do_utt
            )

        if ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                get_common_kate_greeting_utt()
                + what_Kate_can_do_utt
            )
        
        if ctx.config.app_type == AppType.CebM:
            expecting_utterance(get_CebM_kate_intro())

    @staticmethod
    def general_time():
        #start_steps.time_now()
        text_answer_intent_general_time_part1 = "Je přesně "
        text_answer_intent_general_time_part2 = str(start_steps.time_now()[4])
        text_answer_intent_general_time_part3 = ". To máte ještě spoustu času na to si se mnou popovídat. 😉"
        found_texts, _ = get_text_children(find_chat_root())
        time_text = found_texts[0].text.removeprefix(text_answer_intent_general_time_part1).removesuffix(text_answer_intent_general_time_part3)
        time_text = time_text[6:8]
        return text_answer_intent_general_time_part1 + text_answer_intent_general_time_part2 + time_text + text_answer_intent_general_time_part3    

    @staticmethod
    def time_now():
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = str(now.day)
        time = now.strftime("%H:%M")  # H:M
        #date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        return now, year, month, day, time

    @staticmethod
    def general_date():
        # vysledek je v tomto formatu
        #Dnes je čtvrtek, 16. září 2021. Svátek má Ludmila a Lola.
        weekDays = ("pondělí","úterý","středa","čtvrtek","pátek","Sobota","Neděle")
        month_name = ("ledna", "února", "března", "dubna", "května", "června", "července", "srpna", "září", "října", "listopadu", "prosince")
        day_name = str(weekDays[start_steps.time_now()[0].weekday()])
        month_time = month_name[(start_steps.time_now()[0].month)-1]
        general_date = str("Dnes je " + day_name + ", " + start_steps.time_now()[3] + ". " + month_time + " " + start_steps.time_now()[1] + ". Svátek má " + svatek[(start_steps.time_now()[0].month)-1][(start_steps.time_now()[0].day)-1] + ".")
        return general_date

    @staticmethod
    def general_time():
        general_time_part1 = "Je přesně "
        general_time_part3 = ". To máte ještě spoustu času na to si se mnou popovídat. 😉"
        found_texts, _ = get_text_children(find_chat_root())
        general_time_part2 = str(start_steps.time_now()[4])
        time_text = found_texts[0].text.removeprefix(general_time_part1).removesuffix(general_time_part3)[-2:]
        if general_time_part2[0:1] == "0": 
          general_time_part2 = str(start_steps.time_now()[4].removeprefix(start_steps.time_now()[4][0:1]))
        general_time = general_time_part1 + general_time_part2 + ":" + time_text + general_time_part3 
        return general_time

    @staticmethod
    def general_week():
        # need format
        #Máme 37. týden, tedy lichý.
        week_number = int(start_steps.time_now()[0].strftime("%V"))
        if week_number%2 == 1:
            return "Máme " + str(week_number) + ". týden, tedy lichý."
        if week_number%2 == 0:
            return "Máme " + str(week_number) + ". týden, tedy sudý."

    @staticmethod
    def general_year():
        d1 = date.today().timetuple()[7]
        EOY = 365
        if calendar.isleap(d1) is True: EOY = 366
        days_EOY = str(EOY - d1)
        return "Píše se rok " + start_steps.time_now()[1] + " a bude tomu tak ještě " + days_EOY + " dní."

    @staticmethod
    def general_zodiac():
        month = str(start_steps.time_now()[2])
        day = int(start_steps.time_now()[3])

        if (month == "01" and day >= 21)or month=="02" and day <= 20:
            zodiac_signC = "Vodnáře"
            zodiac_signL = "Aquarius"
            end_sign = "21.2"
            next_sign = "Ryby"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "02" and day >= 21)or month=="03" and day <= 20:
            zodiac_signC = "Ryb"
            zodiac_signL = "Pisces"
            end_sign = "21.03"
            next_sign = "Beran"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "03" and day >= 21)or month=="04" and day <= 20:
            zodiac_signC = "Berana"
            zodiac_signL = "Aries"
            end_sign = "21.04"
            next_sign = "Býk"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "04" and day >= 21)or month== "05" and day <= 21:
            zodiac_signC = "Býka"
            zodiac_signL = "Aries"
            end_sign = "22.05"
            next_sign = "Blíženci"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "05" and day >= 22)or month== "06" and day <= 21:
            zodiac_signC = "Blížence"
            zodiac_signL = "Gemini"
            end_sign = "22.06"
            next_sign = "Rak"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "06" and day >= 22)or month=="07" and day <= 22:
            zodiac_signC = "Raka"
            zodiac_signL = "Cancer"
            end_sign = "23.07"
            next_sign = "Lev"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "07" and day >= 23)or month=="08" and day <= 22:
            zodiac_signC = "Lva"
            zodiac_signL = "Leo"
            end_sign = "23.08"
            next_sign = "Panna"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "08" and day >= 23)or month== "09" and day <= 22:
            zodiac_signC = "Panny"
            zodiac_signL = "Virgo"
            end_sign = "23.09"
            next_sign = "Váhy"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "09" and day >= 23)or month== "10" and day <= 23:
            zodiac_signC = "Vah"
            zodiac_signL = "Libra"
            end_sign = "24.10"
            next_sign = "Štír"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "10" and day >= 24)or month == "11" and day <= 22:
            zodiac_signC = "Štíra"
            zodiac_signL = "Scorpius"
            end_sign = "23.11"
            next_sign = "Střelec"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "11" and day >= 23)or month== "12" and day <= 21:
            zodiac_signC = "Střelce"
            zodiac_signL = "Sagittarius"
            end_sign = "22.12"
            next_sign = "Střelec"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")
        elif (month == "12" and day >= 22)or month== "1" and day <= 20:
            zodiac_signC = "Kozoroha"
            zodiac_signL = "Capricornus"
            end_sign = "21.01"
            next_sign = "Vodnář"
            return str("Slunce se teď pohybuje ve znamení " + zodiac_signC +  " (latinsky \"" + zodiac_signL + "\"). Bude tam až do " + end_sign + "., kdy žezlo převezme " + next_sign + ".")

    @staticmethod
    def general_leapyear():
        year = int(start_steps.time_now()[1])
        while start_steps.general_leapyear_last_leapyear(year) != True:
            year = year + 1
        else:
            return "Poslední přestupný rok byl " + str(year-4) + " a příští nás čeká v roce " + str(year) + "."

    @staticmethod
    def general_leapyear_last_leapyear(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                    #"{0} is a leap year".format(year)
                else:
                    return False
                    #"{0} is not a leap year".format(year)
            else:
                return True
                #"{0} is a leap year".format(year)
        else:
            return False
            #"{0} is not a leap year".format(year)

    @staticmethod
    def general_namedayintent_general_nameday():
        #17.9. má svátek Naděžda.
        if str(start_steps.time_now()[3][0:1]) == "0": day_holiday = str(start_steps.time_now()[3][1:2])
        #if str(start_steps.time_now()[4][1:2]) == ":": day_holiday = str(start_steps.time_now()[4][0:1])
        else: day_holiday = str(start_steps.time_now()[3])
        if str(start_steps.time_now()[2][0:1]) == "0": month_holiday = str(start_steps.time_now()[2][1:2])
        else: month_holiday = str(start_steps.time_now()[2])
        return str(day_holiday + ". " + month_holiday + ". má svátek " + svatek[(start_steps.time_now()[0].month)-1][(start_steps.time_now()[0].day)-1] + ".")

    @staticmethod
    def general_isleapyear():
        year = start_steps.time_now()[1]
        leap_year_is = start_steps.find_leap(int(year), True)
        return "Přestupný rok bude až " + str(leap_year_is) + "."

    @staticmethod
    def general_stardate():
        BASE = 58000
        BEGINNING_YEAR = 2005
        # https://www.wikihow.com/Calculate-Stardates
        today = int(start_steps.time_now()[1])
        totalDaysInYear = False
        if calendar.isleap(today) == True: totalDaysInYear = 366
        else: totalDaysInYear = 365
        years = today - BEGINNING_YEAR
        day_of_year = datetime.datetime.now().timetuple().tm_yday
        result = BASE + float(1000) * years + float(1000) / totalDaysInYear * (day_of_year-1)
        vystup = "Hvězdné datum: %.02f" % (result)
        found_texts, _ = get_text_children(find_chat_root())
        text = found_texts[0].text.removeprefix(str(found_texts[0])[-0:-2])[-0:-1]
        return vystup.replace(".", ",").replace(vystup[-1:], text) + "."

    def find_leap(year: int, first: bool):
        if not first and ((year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0)):
            return year
        else:
            return start_steps.find_leap(year+1, False)


    @staticmethod
    def microcase_poem():
        for q in poems_data:
            out = get_text_children(find_chat_root())[0][1].text
            if out == q["part1"]:
                # part1 = str(q["part1"])
                # part2 = str(q["part2"])
                # author_name = str(q["author_name"])
                # poem_name = str(q["poem_name"])
                # book_name = str(q["book_name"])
                # book_year = str(q["book_year"])
                #return part1, part2, author_name, poem_name, book_name, book_year
                return q
        raise Exception("Dind't found Poem")


    @staticmethod
    def intent_microcase_poem_part1():
        #start_steps.run_flow()
        chosen_question = random.choice(intent_microcase_poem)
        send_answer(chosen_question)
        sleep_in_s(3)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        found_poem = start_steps.microcase_poem()
        expecting_utterance(
            microcase_poem
            + Utterance([found_poem["part1"]])
            + what_else_can_I_do_utterance
        )
        return found_poem

@TestSuite
@labels("DoKapsy", "Smart", "CebM")
#@only_this
class smallTalk:
    #@only_this
    def intent_general_time():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_time)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_time = start_steps.general_time()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_time])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_time], ["Co všechno umíš?"])

    #@only_this
    def intent_general_date():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_date)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_date = start_steps.general_date()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_date])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_date], ["Co všechno umíš?"])

    #@only_this
    def intent_general_week():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_week)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_week = start_steps.general_week()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_week])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_week], ["Co všechno umíš?"])

    #@only_this
    def intent_general_month():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_month)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        expecting_utterance(by_appi()["general_month"])

    #@only_this
    def intent_general_zodiac():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_zodiac)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        #"Slunce se teď pohybuje ve znamení Vah (latinsky \"Libra\"). Bude tam až do 24.10., kdy žezlo převezme Štír."
        general_zodiac = start_steps.general_zodiac()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_zodiac])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_zodiac], ["Co všechno umíš?"])

    #@only_this
    def intent_general_year():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_year)
        send_answer(chosen_question)
        # Píše se rok 2021 a bude tomu tak ještě 105 dní.
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_year = start_steps.general_year()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_year])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_year], ["Co všechno umíš?"])

    #@only_this
    def intent_general_isleapyear():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_isleapyear)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_isleapyear = start_steps.general_isleapyear()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_isleapyear])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_isleapyear], ["Co všechno umíš?"])

    #@only_this
    def intent_general_leapyear():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_leapyear)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        general_leapyear = start_steps.general_leapyear()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_leapyear])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_leapyear], ["Co všechno umíš?"])

    #@only_this
    def intent_general_century():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_century)
        send_answer(chosen_question)
        expecting_utterance(by_appi()["general_century"])

    #@only_this
    def intent_general_millennium():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_millennium)
        send_answer(chosen_question)
        general_millennium = "Máme třetí tisíciletí. Pokrok nabral na obrátkách. Přitom všechno, co potřebujeme, už bylo vymyšleno tisíce let před námi. ☸️"
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([general_millennium])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([general_millennium], ["Co všechno umíš?"])

    #@only_this
    #"Hvězdné datum: 74756,16."
    def intent_general_stardate():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_stardate)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        if ctx.config.app_type == AppType.CebM:
            expecting_utterance(
                Utterance([start_steps.general_stardate()], ["Co všechno umíš?"])
            )
        else: 
            expecting_utterance(
                Utterance([start_steps.general_stardate()])
                + what_else_can_I_do_utterance
        )

    #@only_this
    # 17.9. má svátek Naděžda.
    def intent_general_namedayintent_general_nameday():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_namedayintent_general_nameday)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        stardate = start_steps.general_namedayintent_general_nameday()
        if ctx.config.app_type == AppType.DoKapsy or ctx.config.app_type == AppType.Smart:
            expecting_utterance(
                Utterance([stardate])
                + what_else_can_I_do_utterance
            )
        if ctx.config.app_type == AppType.CebM:
            expecting([stardate], ["Co všechno umíš?"])

    #@only_this
    def intent_general_flip_coin_1():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_flip_coin_1)
        send_answer(chosen_question)
        #wait_for_one_of_QABs(["Co všechno umíš?"]) not in ceb?
        expecting_utterance(by_appi()["general_flip_coin_1"])

    #@only_this
    def intent_general_flip_coin_2():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_flip_coin_2)
        send_answer(chosen_question)
        expecting_utterance(by_appi()["general_flip_coin_2"])

    #@only_this
    # Házím kostkou a padla mi 3. 🎲
    #  raise Exception("You cannot have skip and only_this on same TC or TS at the same time.")
    def intent_general_roll_diceintent_general_roll_dice():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_roll_diceintent_general_roll_dice)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])         
        expecting_utterance(by_appi()["hod_kostkou"])

    #@only_this
    def intent_general_joke():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_joke)
        send_answer(chosen_question)
        wait_for_one_of_QABs(["Co všechno umíš?"])
        expecting_utterance(by_appi()["general_joke"])

    # test pro expecting_utterances - dodelani moznosti pridat tuple do mnoziny
    # @only_this
    def intent_general_joke_loop():
        start_steps.run_flow()
        chosen_question = random.choice(intent_general_joke)
        send_answer(chosen_question)
        expecting_utterance(by_appi()["general_joke"])

@TestSuite
@labels("DoKapsy", "Smart")
#@only_this
class smallTalk_K4R:
    def intent_microcase_poem_data():
        found_poem = start_steps.intent_microcase_poem_part1()
        chosen_question = random.choice(intent_general_continue)
        send_answer(chosen_question)
        expecting_utterance(
            Utterance([found_poem["part2"]])
            + what_else_can_I_do_utterance
        )
        chosen_question = random.choice(intent_microcase_author)
        send_answer(chosen_question)
        expecting_utterance(
            Utterance(["Autorem je " + found_poem["author_name"] + "."])
            + what_else_can_I_do_utterance
        )
        chosen_question = random.choice(intent_microcase_name)
        send_answer(chosen_question)
        expecting_utterance(
            Utterance(["Báseň se jmenuje " + found_poem["poem_name"] + "."])
            + what_else_can_I_do_utterance
        )
        chosen_question = random.choice(intent_microcase_collection_name)
        send_answer(chosen_question)
        expecting_utterance(
            Utterance(["Sbírka se jmenuje " + found_poem["book_name"] + " a je z roku " + found_poem["book_year"]+ "."])
            + what_else_can_I_do_utterance
        )

