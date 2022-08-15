from common import *

intent_general_time = [
  "Kolik je hodin?",
  "Jaký je čas?",
  "Kolik je?",
  "co je za čas?",
  "kolik je"
]

intent_general_date =[
  "Kolikátého je?",
  "Co je za den?",
  "Jaký je den?",
  "Co je dneska?",
  "jaky je den",
  "Jaký je dnes den?",
  "Jaký je dneska den",
  "Jaké je datum?"
]

intent_general_week =[
  "Jaký je týden?",
  "číslo týdne",
  "kolikátý je týden?",
  "jaké je číslo týdne",
  "je sudý týden?",
  "je lichý týden?",
  "je sudý nebo lichý týden?"
]

intent_general_month =[
  "Jaký je měsíc?",
  "Co je za měsíc?",
  "Který je měsíc?",
  "co máme za měsíc"
]

intent_general_zodiac =[
  "Jaké je znamení?",
  "Jaké máme znamení?",
  "Znamení zvěrokruhu"
]

intent_general_year = [
  "Jaký je rok?",
  "Co je za rok?",
  "jaký máme rok?",
  "Který je rok?",
  "Jaký je letopočet?",
  "Jaký máme letopočet?",
  "Jaký máme rok?"
]

intent_general_isleapyear = [
  "Je přestupný rok?",
  "máme přestupný rok?",
  "je letos přestupný rok?"
]

intent_general_leapyear = [
  "Kdy je přestupný rok?",
  "Kdy byl přestupný rok?",
  "Kdy bude přestupný rok?"
]

intent_general_century = [
  "Jaké je století?",
  "Co je za století?",
  "Jaké máme století?",
  "Kolikáté je století?",
  "Kolikáté máme století?",
  "Jaképak je století?"
]

intent_general_millennium = [
  "Jaké je tisíciletí?",
  "Co je za tisíciletí?",
  "Jaké máme tisíciletí?",
  "Kolikáté je tisíciletí?",
  "Kolikáté máme tisíciletí?",
  "Jaképak je tisíciletí?"
]

intent_general_stardate = [
  "Jaký je hvězdný čas?",
  "Hvězdné datum",
  "Co je za hvězdné datum",
  "Jaké je hvězdné datum?",
  "Jaké je hvězdné datům?",
  "jake je hvezdne datum"
]

intent_general_namedayintent_general_nameday = [
  "Kdo má dnes svátek?",
  "kdo slaví dnes svátek?",
  "jaký je dnes svátek?",
  "kdo má jmeniny?",
  "kdo ma svatek"
]
intent_general_flip_coin_1 = [
  "Kate hoď mi mincí",
  "Hoď mi mincí",
  "Házej mincí",
  "Hoď mincí",
  "házení mincí",
  "panna nebo orel",
  "orel nebo panna"
]

intent_general_flip_coin_2= [
  "hlava nebo orel",
  "orel nebo hlava"
]

intent_general_roll_diceintent_general_roll_dice =[
  "Kate, hoď mi kostkou",
  "Hoď kostkou",
  "Hoď mi kostku",
  "Hoď mi kostkou",
  "házení kostkou",
  "házej kostkou"
]

intent_general_joke = [
  "Řekni mi vtip",
  "řekni vtip",
  "Pobav mě",
  "Znáš nějaký vtip",
  "Umíš vtipy?",
  "Rozesměj mě",
  "Umíš nějaký vtip?",
  "Další vtip",
  "Ještě jeden vtip",
  "umíš fóry",
  "znáš fóry",
  "řekni mi nějakej fór",
  "další fór",
  "ještě jeden fór",
  "chci vtip",
  "chci se zasmát",
  "zavtipkuj"
]

intent_microcase_poem = [
  "Umíš básničku?",
  "Zarýmuj",
  "Zarecituj mi",
  "Recituj",
  "Řekni básničku",
  "Chci poezii",
  "Chvilka poezie"
]

intent_general_continue = [
  "Pokračuj",
  "Další",
  "Toje vše?"
]

intent_microcase_author = [
  "Od koho to je?",
  "Kdo to složil?",
  "Kdo je autor?",
  "Kdo to napsal?"
]

intent_microcase_name = [
  "Jaké má jméno?",
  "Co to je za báseň?",
  "Jak se to jmenuje?"
]

intent_microcase_collection_name = [
  "Z jaké je to sbírky?",
  "Do jaké sbírky to patří?",
  "Jaká je to sbírka?"
]

# Aswers on jokes
answers_intent_general_joke_utterance = Utterance(
    [
        { # options
            "Co dalšího pro vás mohu udělat?",
            "Co pro vás mohu ještě udělat?",
            "Co pro vás mohu udělat?",
            "Jak mohu dále pomoci?",
            "Co to bude dále?"
        }
    ])

svatek = [
  ["Nový rok, Den obnovy samostatného českého státu", "Karina", "Radmila", "Diana", "Dalimil", "Tři králové", "Vilma", "Čestmír", "Vladan", "Břetislav", "Bohdana", "Pravoslav", "Edita", "Radovan", "Alice", "Ctirad", "Drahoslav", "Vladislav", "Doubravka", "Ilona", "Běla", "Slavomír", "Zdeněk", "Milena", "Miloš", "Zora", "Ingrid", "Otýlie", "Zdislava", "Robin", "Marika"],
  ["Hynek", "Nela", "Blažej", "Jarmila", "Dobromila", "Vanda", "Veronika", "Milada", "Apolena", "Mojmír", "Božena", "Slavěna", "Věnceslav", "Valentýn", "Jiřina", "Ljuba", "Miloslava", "Gizela", "Patrik", "Oldřich", "Lenka", "Petr", "Svatopluk", "Matěj", "Liliana", "Dorota", "Alexandr", "Lumír", "Horymír"],
  ["Bedřich", "Anežka", "Kamil", "Stela", "Kazimír", "Miroslav", "Tomáš", "Gabriela", "Františka", "Viktorie", "Anděla", "Řehoř", "Růžena", "Rút, Matylda", "Ida", "Elena, Herbert", "Vlastimil", "Eduard", "Josef", "Světlana", "Radek", "Leona", "Ivona", "Gabriel", "Marián", "Emanuel", "Dita", "Soňa", "Taťána", "Arnošt", "Kvido"],
  ["Hugo", "Erika", "Richard", "Ivana", "Miroslava", "Vendula", "Heřman, Hermína", "Ema", "Dušan", "Darja", "Izabela", "Julius", "Aleš", "Vincenc", "Anastázie", "Irena", "Rudolf", "Valérie", "Rostislav", "Marcela", "Alexandra", "Evženie", "Vojtěch", "Jiří", "Marek", "Oto", "Jaroslav", "Vlastislav", "Robert", "Blahoslav"],
  ["Svátek práce", "Zikmund", "Alexej", "Květoslav", "Klaudie", "Radoslav", "Stanislav", "Den vítězství", "Ctibor", "Blažena", "Svatava", "Pankrác", "Servác", "Bonifác", "Žofie", "Přemysl", "Aneta", "Nataša", "Ivo", "Zbyšek", "Monika", "Emil", "Vladimír", "Jana", "Viola", "Filip", "Valdemar", "Vilém", "Maxmilián", "Ferdinand", "Kamila"],
  ["Laura", "Jarmil", "Tamara", "Dalibor", "Dobroslav", "Norbert", "Iveta, Slavoj", "Medard", "Stanislava", "Gita", "Bruno", "Antonie", "Antonín", "Roland", "Vít", "Zbyněk", "Adolf", "Milan", "Leoš", "Květa", "Alois", "Pavla", "Zdeňka", "Jan", "Ivan", "Adriana", "Ladislav", "Lubomír", "Petr a Pavel", "Šárka"],
  ["Jaroslava", "Patricie", "Radomír", "Prokop", "Cyril, Metoděj", "Den upálení mistra Jana Husa", "Bohuslava", "Nora", "Drahoslava", "Libuše, Amálie", "Olga", "Bořek", "Markéta", "Karolína", "Jindřich", "Luboš", "Martina", "Drahomíra", "Čeněk", "Ilja", "Vítězslav", "Magdaléna", "Libor", "Kristýna", "Jakub", "Anna", "Věroslav", "Viktor", "Marta", "Bořivoj", "Ignác" ],
  ["Oskar", "Gustav", "Miluše", "Dominik", "Kristián", "Oldřiška", "Lada", "Soběslav", "Roman", "Vavřinec", "Zuzana", "Klára", "Alena", "Alan", "Hana", "Jáchym", "Petra", "Helena", "Ludvík", "Bernard", "Johana", "Bohuslav", "Sandra", "Bartoloměj", "Radim", "Luděk", "Otakar", "Augustýn", "Evelína", "Vladěna", "Pavlína"],
  ["Linda, Samuel", "Adéla", "Bronislav", "Jindřiška", "Boris", "Boleslav", "Regína", "Mariana", "Daniela", "Irma", "Denisa", "Marie", "Lubor", "Radka", "Jolana", "Ludmila", "Naděžda", "Kryštof", "Zita", "Oleg", "Matouš", "Darina", "Berta", "Jaromír a Jaromíra", "Zlata", "Andrea", "Jonáš", "Václav, Den české státnosti", "Michal", "Jeroným"],
  ["Igor", "Olivie, Oliver", "Bohumil", "František", "Eliška", "Hanuš", "Justýna", "Věra", "Štefan, Sára", "Marina", "Andrej", "Marcel", "Renáta", "Agáta", "Tereza", "Havel", "Hedvika", "Lukáš", "Michaela", "Vendelín", "Brigita", "Sabina", "Teodor", "Nina", "Beáta", "Erik", "Šarlota, Zoe", "Den vzniku samostatného československého státu", "Silvie", "Tadeáš", "Štěpánka"],
  ["Felix", "Památka zesnulých (dušičky)", "Hubert", "Karel a Karla", "Miriam", "Liběna", "Saskie", "Bohumír", "Bohdan", "Evžen", "Martin", "Benedikt", "Tibor", "Sáva", "Leopold", "Otmar", "Mahulena, Den boje za svobodu a demokracii", "Romana", "Alžběta", "Nikola", "Albert", "Cecílie", "Klement", "Emílie", "Kateřina", "Artur", "Xenie", "René", "Zina", "Ondřej"],
  ["Iva", "Blanka", "Svatoslav", "Barbora", "Jitka", "Mikuláš", "Benjamín", "Květoslava", "Vratislav", "Julie", "Dana", "Simona", "Lucie", "Lýdie", "Radana", "Albína", "Daniel", "Miloslav", "Ester", "Dagmar", "Natálie", "Šimon", "Vlasta", "Adam, Eva, Štědrý den", "1. svátek vánoční", "Štěpán, 2. svátek vánoční", "Žaneta", "Bohumila", "Judita", "David", "Silvestr" ]]

hod_kostkou = Utterance(
    [
        { # options
            "Házím kostkou a padla mi 1. 🎲",
            "Házím kostkou a padla mi 2. 🎲",
            "Házím kostkou a padla mi 3. 🎲",
            "Házím kostkou a padla mi 4. 🎲",
            "Házím kostkou a padla mi 5. 🎲",
            "Házím kostkou a padla mi 6. 🎲"
        }
    ]
) + what_else_can_I_do_utterance

general_month = Utterance(
    [
        { # options
        "Je leden. Leden studený, duben zelený. 🌱",
        "Je únor. Únor bílý, pole sílí. 🌾",
        "Je březen. Březen, za kamna vlezem. 🔥",
        "Je duben. Duben, ještě tam budem. ☔",
        "Je máj, lásky čas. 🥰",
        "Je červen. Červen-li více sucho než mokro bývá, urodí se hojnost dobrého vína. 🤩",
        "Je červenec. Co červenec neupeče, to již srpnu neuteče. 🏃",
        "Je srpen. V srpnu když půlnoční vítr věje, bez deště slunéčko hřeje. 🌞",
        "Je září. Teplé září - dobře se ovoci i vínu daří. 🍇",
        "Je říjen. Čím déle vlaštovky u nás v říjnu prodlévají, tím déle pěkné a jasné dny potrvají. 🐦",
        "Je listopad. Když ještě v listopadu hřmívá, úrodný rok nato bývá. 🌩️",
        "Je prosinec. Mléčná dráha v prosinci jasná, bude v příštím roce úroda krásná. 🌌"
        }
    ]
) + what_else_can_I_do_utterance

general_flip_coin_1 = Utterance(
    [
        "Házím mincí... a je to... 👀",
        { # options
        "Panna 🙍\u200d♀️",
        "Orel 🦅",
        "Hrana ➖"
        }
    ]
) + what_else_can_I_do_utterance

general_flip_coin_2 = Utterance(
        [
            "Házím mincí... a je to... 👀",
            { # options
            "Hlava 👩",
            "Orel 🦅"
            }
        ]
      ) + what_else_can_I_do_utterance

general_century = Utterance(
        [
          { # options
          "Máme dvacáté první století. Dříve byla základní lidská potřeba jídlo a pití. Dneska si bez internetu už pomalu ani neuvaříte. 😅"
          }
        ]
      ) + what_else_can_I_do_utterance

def by_appi():
  if ctx.config.app_type == AppType.DoKapsy: 
    DoKapsy_dictionary = {
    "general_flip_coin_2": 
      general_flip_coin_2,
    "general_flip_coin_1":
      general_flip_coin_1, 
    "general_century":
      general_century,
    "hod_kostkou":
      hod_kostkou,
    "general_joke":
      general_joke,
    "general_month":
      general_month
    }
    return DoKapsy_dictionary

  if ctx.config.app_type == AppType.Smart: 
    Smart_dictionary = {
    "general_flip_coin_2": 
      general_flip_coin_2,
    "general_flip_coin_1":
      general_flip_coin_1,
    "general_century":
      general_century,
    "hod_kostkou":
      hod_kostkou,
    "general_joke":
      general_joke,
    "general_month":
      general_month
    
    }
    return Smart_dictionary

  if ctx.config.app_type == AppType.CebM:
    CebM_dictionary = {
    "general_flip_coin_2":
      Utterance(
        [
          "Házím mincí... a je to... 👀",
          { # options
          "Hlava 👩",
          "Orel 🦅"
          }
        ], ["Co všechno umíš?"]
    ),
    "general_flip_coin_1":
      Utterance(
        [
          "Házím mincí... a je to... 👀",
          { # options
          "Panna 🙍\u200d♀️",
          "Orel 🦅",
          "Hrana ➖"
          }
        ], ["Co všechno umíš?"]
      ),
    "general_century":
      Utterance(
        ["Máme dvacáté první století. Dříve byla základní lidská potřeba jídlo a pití. Dneska si bez internetu už pomalu ani neuvaříte. 😅"], ["Co všechno umíš?"]),

    "hod_kostkou":
      Utterance(
          [
              { # options
                  "Házím kostkou a padla mi 1. 🎲",
                  "Házím kostkou a padla mi 2. 🎲",
                  "Házím kostkou a padla mi 3. 🎲",
                  "Házím kostkou a padla mi 4. 🎲",
                  "Házím kostkou a padla mi 5. 🎲",
                  "Házím kostkou a padla mi 6. 🎲"
              }
          ], ["Co všechno umíš?"]
      ),

    "general_joke":
      Utterance([
        { # options
        "Co říká 0 osmičce? Hezký opasek. 🤣",
        "Smoothie. Způsob, jak prodat dvě broskve za devadesát korun. 🤣",
        "Nejlepší vynález jsou eskalátory, protože se nemůžou nikdy rozbít... Mohou se z nich maximálně stát obyčejné schody. 🤣",
        "Minulý měsíc jsem si dala předsevzetí, že zhubnu 10 kilo. Už mi zbývá jen 15. Cha! 🤣",
        "Chuck Norris je jediný člověk, co došel z USA do USB! 🤣",
        "Víte, jak jezdí Chuck Norris v zimě na lyžařském vleku? Předjíždí! 🤣",
        "Potkají se dva psi a jeden druhému říká: „Kam jdeš?“\n\n„S blechama k veterináři.“\n\n„To je zvláštní, já je mám dva roky a ještě mi neonemocněly!“ 🤣",
        "Helium vejde do baru a barman říká:\n\n„Vzácné plyny neobsluhujeme!“\n\nHelium nereaguje. 🤣",
        "Jdou dva transformeři z hospody a ten jeden tomu druhýmu povídá: „Pojď, složíme se na taxík.“ 🤣",
        "Ptá se želva dinosaura: „Hej, dinosaure, dal si tě Noe do přátel?“\n\n„Ne.“\n\n„Hm. Tak to máš blbý...“ 🤣",
        "Nastoupí pán do taxíku a řidič mu hned povídá: „Dobrý den, omlouvám se za ten smrad z dezinfekce.“\n\nChlápek na to odpovídá: „To je v pohodě, já stejně už několik dní vůbec nic necítím.“ 🤣",
        (
          "Potká myška myšku a ta první říká: „Tak jsem ti potkala takovýho prima myšáka.“\n\n„A máš fotku?“\n\n...",
          "„Vždyť je to netopýr!“\n\n„Ten prevít! A mně říkal, že je pilot!“ 🤣"
          ),
        "Pan Novotný se ohlásí na personálním oddělení: „Jsem přesvědčen, že můj plat neodpovídá mým schopnostem!“\n\n„Také jsme to zjistili, ale přeci vás nemůžeme nechat umřít hlady!“ 🤣",
        (
          "Prochází se policajt po parku a uvidí muže, který v ruce drží tučňáka.\n\n„Dnes ráno jsem ho našel, co s ním mám udělat?“ zeptal se muž.„Vezměte ho do ZOO,“ poradí policajt.",
          "Druhý den se znovu prochází po parku a znovu vidí muže s tučňákem.\n\n„Proč jste ho nevzal do ZOO?“ nechápe policajt.\n\n„Tam jsem s ním byl včera. Dneska jdeme do kina.“ 🤣"
        ),
        "Víte, jak dělá kočka? Mňau.\n\nVíte, jak dělá pes? Haf, Haf.\n\nVíte, jak dělá liška? Na těchto základech můžete stavět. 🤣",
        "„Mami, kup mi velblouda!“\n\n„A čím bychom ho krmili?“\n\n„Tak mi kup toho ze zoologické zahrady, ten se krmit nesmí!“ 🤣",
        "Řekla bych vám skvělý vtip o cestování časem. Ale vám se nelíbil. 🤣",
        "Chucku Norrisovi se jednou při seskoku z letadla neotevřel padák. Hned druhý den ho šel reklamovat. 🤣",
        "„Mamí, upadl nám žebřík,“ říká Pepíček. „Tak to řekni tátovi!“ „On už to ví, visí na okapu.“ 🤣",
        "Když Alexander Graham Bell vynalezl telefon, zjistil, že má 2 zmeškané hovory od Chucka Norrise. 🤣",
        "Čech a Američan hrají šachy. Američan táhne a říká: „Jezdec na D1!“ Čech to komentuje: „To bych nedělal...“ 🤣"
        }
      ], ["Co všechno umíš?"]),
      "general_month":
        Utterance(
          [
              { # options
              "Je leden. Leden studený, duben zelený. 🌱",
              "Je únor. Únor bílý, pole sílí. 🌾",
              "Je březen. Březen, za kamna vlezem. 🔥",
              "Je duben. Duben, ještě tam budem. ☔",
              "Je máj, lásky čas. 🥰",
              "Je červen. Červen-li více sucho než mokro bývá, urodí se hojnost dobrého vína. 🤩",
              "Je červenec. Co červenec neupeče, to již srpnu neuteče. 🏃",
              "Je srpen. V srpnu když půlnoční vítr věje, bez deště slunéčko hřeje. 🌞",
              "Je září. Teplé září - dobře se ovoci i vínu daří. 🍇",
              "Je říjen. Čím déle vlaštovky u nás v říjnu prodlévají, tím déle pěkné a jasné dny potrvají. 🐦",
              "Je listopad. Když ještě v listopadu hřmívá, úrodný rok nato bývá. 🌩️",
              "Je prosinec. Mléčná dráha v prosinci jasná, bude v příštím roce úroda krásná. 🌌"
              }
          ],
          ["Co všechno umíš?"]
      )
    }
    return CebM_dictionary

general_joke = Utterance([
  { # options
  "Co říká 0 osmičce? Hezký opasek. 🤣",
  "Smoothie. Způsob, jak prodat dvě broskve za devadesát korun. 🤣",
  "Nejlepší vynález jsou eskalátory, protože se nemůžou nikdy rozbít... Mohou se z nich maximálně stát obyčejné schody. 🤣",
  "Minulý měsíc jsem si dala předsevzetí, že zhubnu 10 kilo. Už mi zbývá jen 15. Cha! 🤣",
  "Chuck Norris je jediný člověk, co došel z USA do USB! 🤣",
  "Víte, jak jezdí Chuck Norris v zimě na lyžařském vleku? Předjíždí! 🤣",
  "Potkají se dva psi a jeden druhému říká: „Kam jdeš?“\n\n„S blechama k veterináři.“\n\n„To je zvláštní, já je mám dva roky a ještě mi neonemocněly!“ 🤣",
  "Helium vejde do baru a barman říká:\n\n„Vzácné plyny neobsluhujeme!“\n\nHelium nereaguje. 🤣",
  "Jdou dva transformeři z hospody a ten jeden tomu druhýmu povídá: „Pojď, složíme se na taxík.“ 🤣",
  "Ptá se želva dinosaura: „Hej, dinosaure, dal si tě Noe do přátel?“\n\n„Ne.“\n\n„Hm. Tak to máš blbý...“ 🤣",
  "Nastoupí pán do taxíku a řidič mu hned povídá: „Dobrý den, omlouvám se za ten smrad z dezinfekce.“\n\nChlápek na to odpovídá: „To je v pohodě, já stejně už několik dní vůbec nic necítím.“ 🤣",
  (
    "Potká myška myšku a ta první říká: „Tak jsem ti potkala takovýho prima myšáka.“\n\n„A máš fotku?“\n\n...",
    "„Vždyť je to netopýr!“\n\n„Ten prevít! A mně říkal, že je pilot!“ 🤣"
  ),
  "Pan Novotný se ohlásí na personálním oddělení: „Jsem přesvědčen, že můj plat neodpovídá mým schopnostem!“\n\n„Také jsme to zjistili, ale přeci vás nemůžeme nechat umřít hlady!“ 🤣",
  (
    "Prochází se policajt po parku a uvidí muže, který v ruce drží tučňáka.\n\n„Dnes ráno jsem ho našel, co s ním mám udělat?“ zeptal se muž.„Vezměte ho do ZOO,“ poradí policajt.",
    "Druhý den se znovu prochází po parku a znovu vidí muže s tučňákem.\n\n„Proč jste ho nevzal do ZOO?“ nechápe policajt.\n\n„Tam jsem s ním byl včera. Dneska jdeme do kina.“ 🤣"
  ),
  "Víte, jak dělá kočka? Mňau.\n\nVíte, jak dělá pes? Haf, Haf.\n\nVíte, jak dělá liška? Na těchto základech můžete stavět. 🤣",
  "„Mami, kup mi velblouda!“\n\n„A čím bychom ho krmili?“\n\n„Tak mi kup toho ze zoologické zahrady, ten se krmit nesmí!“ 🤣",
  "Řekla bych vám skvělý vtip o cestování časem. Ale vám se nelíbil. 🤣",
  "Chucku Norrisovi se jednou při seskoku z letadla neotevřel padák. Hned druhý den ho šel reklamovat. 🤣",
  "„Mamí, upadl nám žebřík,“ říká Pepíček. „Tak to řekni tátovi!“ „On už to ví, visí na okapu.“ 🤣",
  "Když Alexander Graham Bell vynalezl telefon, zjistil, že má 2 zmeškané hovory od Chucka Norrise. 🤣",
  "Čech a Američan hrají šachy. Američan táhne a říká: „Jezdec na D1!“ Čech to komentuje: „To bych nedělal...“ 🤣"
  }
]) + what_else_can_I_do_utterance

intent_microcase_poem = [
  "Umíš básničku?",
  "Zarýmuj",
  "Zarecituj mi",
  "Recituj",
  "Řekni básničku",
  "Chci poezii",
  "Chvilka poezie"
]

intent_general_continue = [
  "Pokračuj",
  "Další",
  #"To je vše?"
]

intent_microcase_author = [
  "Od koho to je?",
  "Kdo to složil?",
  "Kdo je autor?",
  "Kdo to napsal?"
]

intent_microcase_name = [
  "Jaké má jméno?",
  "Co to je za báseň?",
  "Jak se to jmenuje?"
]

intent_microcase_collection_name = [
  "Z jaké je to sbírky?",
  "Do jaké sbírky to patří?",
  "Jaká je to sbírka?"
]


microcase_poem = Utterance([
  { # options
  "Ráda vám zarecituji báseň. Co třeba tuhle.",
  "To mě těší, že se zajímáte o poezii. Já mám nejraději tuhle."
  }
])

poems_data = [
  {
  "part1": "Znám křišťálovou studánku,\nkde nejhlubší je les,\ntam roste tmavé kapradí\na vůkol rudý vřes.",
  "part2": "Tam ptáci, laně chodí pít\npod javorový kmen,\nti ptáci za dne bílého,\nty laně v noci jen.\n\nKdyž usnou lesy hluboké\na kolem ticho jest,\ntu nebesa i studánka\njsou plny zlatých hvězd.",
  "author_name": "Josef Václav Sládek",
  "poem_name" : "Lesní studánka",
  "book_name": "Zvony a zvonky",
  "book_year": "1894"
  },
  {
  "part1": "Já jsem děvče okaté,\nšatečky mám strakaté,\nvypadám v nich celičká\njak ta lesní pěnička.",
  "part2": "Já jsem děvče okaté,\ntvářičky mám buclaté,\nna nich jako růže květ,\na mne těší celý svět!",
  "author_name": "Josef Václav Sládek",
  "poem_name" : "Okáč",  
  "book_name": "Zvony a zvonky",
  "book_year": "1894"    
  }
]