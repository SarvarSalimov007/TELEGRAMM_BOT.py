"""
So'kinish va reklama filtrlari
"""

import re


class ProfanityFilter:
    """So'kinish so'zlarini aniqlash"""
    
    def __init__(self):
        # So'kinish so'zlari ro'yxati (maksimal to'liq ro'yxat)
        self.bad_words = [
            # ========== RUS TILIDA ==========
            # Keng tarqalgan
            'блять', 'блядь', 'бля', 'бляд', 'блядина', 'блядки',
            'хуй', 'хуя', 'хуе', 'хуйня', 'хуйло', 'хуёв', 'хуев',
            'хуярить', 'хуёвый', 'хуйнутый', 'хуйнуть',
            'пизда', 'пиздец', 'пизд', 'пизду', 'пиздануть',
            'ебать', 'ебаный', 'ебан', 'ебал', 'ебало', 'ебать',
            'ебанутый', 'ебанько', 'еблан', 'еблань', 'ебливый',
            'сука', 'сукин', 'сук', 'сучара', 'сучий',
            'пидор', 'пидорас', 'пидарас', 'пидр', 'пидрила',
            'мразь', 'мразота', 'мрази',
            'падла', 'падлюка', 'падло',
            'долбоеб', 'долбоёб', 'долбаеб', 'долбаёб',
            'говно', 'говнюк', 'говнарь',
            'говноед', 'говноедка',
            'залупа', 'залупка',
            'мудак', 'мудила', 'мудачье',
            'ублюдок', 'ублюдочный',
            'тварь', 'твари',
            'мраз', 'мразь',
            'уебок', 'уебан',
            'похуй', 'похуист',
            'ебашка', 'ебануть',
            'заебись', 'заебал',
            'ебанулся', 'ебанулся',
            'проеб', 'проебал',
            'выебан', 'выебываться',
            'подъеб', 'подъебал',
            'заебать', 'заебали',
            'выебывайся',
            'ебатьврот', 'ебанутка', 'ебашить',
            'ебланка', 'ебля', 'ебучая',
            'ебнутый', 'ебнулся', 'ебучий',
            'ебанусь', 'ебаная', 'ебаный',
            'заебался', 'заебалась', 'заебались',
            'выебать', 'выебал', 'выебала',
            'перееб', 'переебать',
            'доёб', 'доёбаться',
            'наёб', 'наёбывать',
            'объебать', 'объеб',
            'разъеб', 'разъебать',
            'хуйня', 'хуярить', 'хуёвый',
            'похую', 'похер',
            'хуесос', 'хуесосить',
            'пиздюк', 'пиздюлей',
            'ебут', 'ебёшь',
            'ебёт', 'ебём',
            'ебёте', 'ебут',
            'обоссать', 'обоссался',
            'обосрать', 'обосрался',
            'ссышь', 'ссыте',
            'обосранный',
            
            # ========== INGLIZ TILIDA ==========
            # Asosiy
            'fuck', 'fucking', 'fucked', 'fucker', 'fuckers',
            'fuckin', 'fucks', 'fuckup', 'fuckwit',
            'shit', 'shits', 'shitting', 'shitty', 'shitter',
            'damn', 'damned', 'damnit', 'dammit',
            'bitch', 'bitches', 'bitching', 'bitchy',
            'asshole', 'ass', 'asses', 'asshole',
            'dick', 'dicks', 'dickhead', 'dickwad',
            'pussy', 'pussies', 'puss',
            'cunt', 'cunts', 'cunting',
            'motherfucker', 'motherfuckers', 'motherfucking',
            'bastard', 'bastards', 'bastardy',
            'whore', 'whores', 'whoring', 'whorehouse',
            # Qo'shimcha
            'slut', 'sluts', 'slutty',
            'bitchass', 'asshat',
            'cock', 'cocks', 'cockhead',
            'prick', 'pricks',
            'douche', 'douchebag', 'douchebags',
            'dumbass', 'dumbasses',
            'fag', 'fags', 'faggot', 'faggots',
            'nigger', 'niggers', 'nigga', 'niggas',
            'retard', 'retards', 'retarded',
            'stupid', 'stupids',
            'idiot', 'idiots', 'idiotic',
            'moron', 'morons',
            'jackass', 'jackasses',
            'asswipe', 'asswipes',
            'bullshit', 'bullshits',
            'crap', 'craps',
            'hell', 'hells',
            'screw', 'screws', 'screwed',
            'suck', 'sucks', 'sucker', 'suckers',
            'darn', 'darned',
            'goddamn', 'goddamned',
            'bloody',
            'bugger', 'buggers',
            'piss', 'pissed', 'pissing',
            'wank', 'wanker', 'wanking',
            'twat', 'twats',
            'bollocks', 'bollock',
            'cocksucker', 'cocksuckers',
            'shitbag', 'shitbags',
            'fucknut', 'fucknuts',
            'fucktard', 'fucktards',
            'shitstain', 'shitstains',
            'fuckstick', 'fucksticks',
            'dickslap', 'dickslaps',
            'motherfuck', 'motherfucks',
            'bullcrap', 'bullcraps',
            'horseshit', 'horseshits',
            'dogshit', 'dogshits',
            'chickenshit', 'chickenshits',
            'apeshit', 'apeshits',
            'batshit', 'batshits',
            'nutcase', 'nutcases',
            'freak', 'freaks', 'freaking', 'freaked',
            'weirdo', 'weirdos',
            'loser', 'losers',
            'dummy', 'dummies',
            'jerk', 'jerks', 'jerking', 'jerked', 'jerky',
            'scumbag', 'scumbags',
            'scum', 'scums',
            'trash', 'trashes', 'trashy',
            'scumball', 'scumballs',
            'dickface', 'dickfaces',
            'fuckhead', 'fuckheads',
            'shitbag', 'shitbags',
            'dumbfuck', 'dumbfucks',
            'fucktard', 'fucktards',
            'shitbrain', 'shitbrains',
            'assface', 'assfaces',
            'buttface', 'buttfaces',
            'fucktoy', 'fucktoys',
            'fuckup', 'fuckups',
            'shitstain', 'shitstains',
            'pisshead', 'pissheads',
            'pissface', 'pissfaces',
            'wankstain', 'wankstains',
            'wankface', 'wankfaces',
            'cuntface', 'cuntfaces',
            'twatwaffle', 'twatwaffles',
            'dickmunch', 'dickmunches',
            'fuckwad', 'fuckwads',
            'shitstirrer', 'shitstirrers',
            'cockmonger', 'cockmongers',
            'assclown', 'assclowns',
            'dumbshit', 'dumbshits',
            'smartass', 'smartasses',
            'dumbass', 'dumbasses',
            'loudmouth', 'loudmouths',
            'hothead', 'hotheads',
            'bonehead', 'boneheads',
            'shitheel', 'shitheels',
            'cuntrag', 'cuntrags',
            'fuckboy', 'fuckboys',
            'asshat', 'asshats',
            'dickweed', 'dickweeds',
            'cocksmoker', 'cocksmokers',
            'motherhumper', 'motherhumpers',
            'sisterfucker', 'sisterfuckers',
            'fatherfucker', 'fatherfuckers',
            'cockslap', 'cockslaps',
            'ballsack', 'ballsacks',
            'nutsack', 'nutsacks',
            'dickwad', 'dickwads',
            'fuckwit', 'fuckwits',
            'shitwit', 'shitwits',
            'fuckknuckle', 'fuckknuckles',
            'shitsack', 'shitsacks',
            'cumdumpster', 'cumdumpsters',
            'cumbucket', 'cumbuckets',
            'cumslut', 'cumsluts',
            'cumdump', 'cumdumps',
            'cumsock', 'cumsocks',
            'spermwhale', 'spermwhales',
            'fuckboy', 'fuckboys',
            'fuckgirl', 'fuckgirls',
            'fuckbuddy', 'fuckbuddies',
            'fuckhole', 'fuckholes',
            'asslicker', 'asslickers',
            'bootlicker', 'bootlickers',
            'brownnoser', 'brownnosers',
            'asskisser', 'asskissers',
            'dicklicker', 'dicklickers',
            'cuntlicker', 'cuntlickers',
            'pussylicker', 'pussylickers',
            'rimjob', 'rimjobs',
            'buttmunch', 'buttmunches',
            'assmunch', 'assmunches',
            
            # ========== O'ZBEK TILIDA ==========
            'ahmoq', 'ahmoqlar', 'ahmoqona',
            'yomon', 'yomonlik',
            'keraksiz', 'keraksizlik',
            'bekorchi', 'bekorchilik',
            'stupid',
            'johil',
            'gapirovchi',
            'yomonlashmoq', 'yomonlash',
            'ahmoqlashmoq', 'ahmoqlash',
            # Qo'shimcha o'zbekcha so'kinish so'zlari
            'iflos', 'ifloslik',
            'qo\'toq', 'qo\'toqbosh', 'qotoq', 'qotoqbosh',
            'ko\'t', 'kot', 'ko\'tikatta', 'kotikatta',
            'onangnisikay',
            'sikama',
            'jalab', 'jalablik',
            'suka',
            'xaromi', 'harom', 'xarom',
            'onangnieshshaksiksin',
            'pidaraz', 'pidaras'
            
            # ========== TRANSLITERATSIYA (rus -> latin) ==========
            'blyat', 'blyad', 'blya', 'blyad',
            'huy', 'hue', 'huev',
            'pizda', 'pizdec', 'pizd',
            'ebat', 'ebany', 'eban',
            'suka', 'sukin', 'suk',
            'pidor', 'pidoras', 'pidar',
            'eblan', 'eblanь', 'eblaniy',
            'mraz', 'mrazь',
            'padla', 'padlo',
            'dolboeb', 'dolbёb',
            'govno', 'govnuk',
            'zalupa',
            'mudak', 'mudila',
            'ublyudok',
            'tvar',
            'uebok', 'ueban',
            'pohuy',
            'ebanka',
            'ebanutka', 'ebatvrot',
            'zayebalsya', 'zayebalsya',
            'viebat', 'viebal',
            'pereyeb', 'pereyebat',
            'doyob', 'doyobatsya',
            'nayob', 'nayobivat',
            'obyebat', 'obyeb',
            'razeyeb', 'razeyebat',
            'huyesos', 'huyesosit',
            'pizdyuk', 'pizdyuley',
            'obosrat', 'obossat',
            'ssish', 'ssite',
            'obosranniy',
            
            # ========== QISQARTMALAR VA VARIANTLAR ==========
            'fck', 'fckn', 'fk',
            'sht', 'sh1t',
            'b1tch', 'btch',
            'd1ck', 'dck',
            'pssy', 'pssy',
            'cnt', 'c*nt',
            'mthrfckr', 'mthrfkr',
            'n1gg3r', 'n1gga', 'n*gga',
            'r3tard', 'ret*rd',
            'stpid', 'stup*d',
            'a$$', 'a$$hole',
            'd*ck', 'd*ckhead',
            'p*ssy',
            'c*nt',
            'f*ck', 'f*cking', 'f*cked',
            'sh*t', 'sh*tting',
            'b*tch',
            'a**hole', 'a**',
            'd*mn',
            'f@ck', 'f@cking',
            'sh!t', 'sh!tting',
            'b!tch', 'b!tches',
            'd!ck', 'd!ckhead',
            'a$$', 'a$$hole',
            'f***', 'f***ing',
            's***', 's***ting',
            'b***', 'b***es',
            'd***', 'd***head',
            'p***', 'p***y',
            'c***', 'c***s',
            'm***', 'm***erf***er',
            'n***', 'n***a',
            'r***', 'r***ed',
            'h0m0', 'h0m0s',
            'g@y', 'g@ys',
            'l3wd', 'l3wds',
            'p0rn', 'p0rn0',
            's3x', 's3xy',
            's3xual',
            
            # ========== KIRILL ALIFBOSI BILAN YOZILGAN INGLIZ SO'ZLARI ==========
            'fuсk', 'shіt', 'dаmn', 'bіtch',
            'аss', 'dіck', 'puѕsy', 'сunt',
            'mоthеrfuckеr',
            'ахмок', 'йомон', 'кераксиз',
            
            # ========== SO'ZLAR KOMBINATSIYALARI ==========
            'еблань', 'ебанутый', 'ебанулся',
            'хуйня', 'хуйло', 'хуёвый',
            'пиздец', 'пиздануть',
            'блядь', 'блядина',
            'сучара', 'сучий',
            'долбоеб', 'долбоёб',
            'говноед',
            'уебок', 'уебан',
            'похуй', 'похуист',
            
            # ========== NUMBERS BILAN ALMASHTIRILGAN ==========
            'f0ck', 'f0cking',
            'sh1t', 'sh1tting',
            'b1tch', 'b1tches',
            'd1ck', 'd1ckhead',
            'p0rn', 'p0rn0',
            'a55', 'a55hole',
            'n1gg3r', 'n1gga',
            'n1gg@', 'n1gg@r',
            'f4ck', 'f4cking',
            'sh1tt', 'sh1tt1ng',
            'b1tch3s', 'b1tch3s',
            'd1ckh3@d',
            'a55h0l3', 'a55h0le',
            'm0th3rf*ck3r',
            'c0ck', 'c0cks',
            'pr1ck', 'pr1cks',
            'tw4t', 'tw4ts',
            'c*nt5', 'c*nts',
            'f*ck3r', 'f*ck3rs',
            'sh*tb4g', 'sh*tb4gs',
            'd1ckw3ed', 'd1ckw3eds',
            '4ss', '4ss3s', '4ssh0l3',
            'f*ckf4c3', 'f*ckf4ces',
            'sh*tf4c3', 'sh*tf4ces',
            'd1ckf4c3', 'd1ckf4ces',
            'c*ntf4c3', 'c*ntf4ces',
            'p*ssyf4c3', 'p*ssyf4ces',
            
            # ========== YANA QO'SHIMCHA ==========
            'cock', 'cocksucker', 'cocksucking',
            'turd', 'turds',
            'wank', 'wanker', 'wankers',
            'tosser', 'tossers',
            'bellend', 'bellends',
            'knob', 'knobhead',
            'git', 'gits',
            'pillock', 'pillocks',
            'plonker', 'plonkers',
            'berk', 'berks',
            'muppet', 'muppets',
            'dipshit', 'dipshits',
            'dumbfuck', 'dumbfucks',
            'shithead', 'shitheads',
            'dickweed', 'dickweeds',
            'fuckface', 'fuckfaces',
            'shitface', 'shitfaces',
            'assclown', 'assclowns',
            'douchenozzle', 'douchenozzles',
            'fuckery', 'fuckerys',
            'shittery', 'shitterys',
            'cuntery', 'cunterys',
            'dickery', 'dickerys',
            'assery', 'asserys',
            'pissery', 'pisserys',
            'wankery', 'wankerys',
            'bullshitter', 'bullshitters',
            'shitforbrains', 'shitforbrainss',
            'dickforbrains', 'dickforbrainss',
            'assforbrains', 'assforbrainss',
            'fucktardery', 'fucktarderys',
            'cocksucking', 'cocksuckings',
            'motherfucking', 'motherfuckings',
            'sisterfucking', 'sisterfuckings',
            'fatherfucking', 'fatherfuckings',
            'brotherfucking', 'brotherfuckings',
            'fuckbucket', 'fuckbuckets',
            'shitbucket', 'shitbuckets',
            'dickbucket', 'dickbuckets',
            'cuntbucket', 'cuntbuckets',
            'assbucket', 'assbuckets',
            'pissbucket', 'pissbuckets',
            'wankbucket', 'wankbuckets',
            'fuckstain', 'fuckstains',
            'dickstain', 'dickstains',
            'cuntstain', 'cuntstains',
            'assstain', 'assstains',
            'pissstain', 'pissstains',
            'wankstain', 'wankstains',
            'fuckrag', 'fuckrags',
            'dickrag', 'dickrags',
            'cuntrag', 'cuntrags',
            'assrag', 'assrags',
            'pissrag', 'pissrags',
            'wankrag', 'wankrags',
            'fuckslut', 'fucksluts',
            'shitslut', 'shitsluts',
            'dickslut', 'dicksluts',
            'cuntslut', 'cuntsluts',
            'assslut', 'asssluts',
            'pissslut', 'pisssluts',
            'wankslut', 'wanksluts',
            'fuckwhore', 'fuckwhores',
            'shitwhore', 'shitwhores',
            'dickwhore', 'dickwhores',
            'cuntwhore', 'cuntwhores',
            'asswhore', 'asswhores',
            'pisswhore', 'pisswhores',
            'wankwhore', 'wankwhores',
            'fuckpig', 'fuckpigs',
            'shitpig', 'shitpigs',
            'dickpig', 'dickpigs',
            'cuntpig', 'cuntpigs',
            'asspig', 'asspigs',
            'pisspig', 'pisspigs',
            'wankpig', 'wankpigs',
            'fuckmonkey', 'fuckmonkeys',
            'shitmonkey', 'shitmonkeys',
            'dickmonkey', 'dickmonkeys',
            'cuntmonkey', 'cuntmonkeys',
            'assmonkey', 'assmonkeys',
            'pissmonkey', 'pissmonkeys',
            'wankmonkey', 'wankmonkeys',
            'fucknugget', 'fucknuggets',
            'shitnugget', 'shitnuggets',
            'dicknugget', 'dicknuggets',
            'cuntnugget', 'cuntnuggets',
            'assnugget', 'assnuggets',
            'pissnugget', 'pissnuggets',
            'wanknugget', 'wanknuggets',
            'fucktard', 'fucktards',
            'shittard', 'shittards',
            'dicktard', 'dicktards',
            'cunttard', 'cunttards',
            'asstard', 'asstards',
            'pisstard', 'pisstards',
            'wanktard', 'wanktards',
            'fucksack', 'fucksacks',
            'shitsack', 'shitsacks',
            'dicksack', 'dicksacks',
            'cuntsack', 'cuntsacks',
            'asssack', 'asssacks',
            'pisssack', 'pisssacks',
            'wanksack', 'wanksacks',
            'fuckhole', 'fuckholes',
            'shithole', 'shitholes',
            'dickhole', 'dickholes',
            'cunthole', 'cuntholes',
            'asshole', 'assholes',
            'pisshole', 'pissholes',
            'wankhole', 'wankholes',
            'fucksmear', 'fucksmears',
            'shitsmear', 'shitsmears',
            'dicksmear', 'dicksmears',
            'cuntsmear', 'cuntsmears',
            'asssmear', 'asssmears',
            'pisssmear', 'pisssmears',
            'wanksmear', 'wanksmears',
            'fuckwad', 'fuckwads',
            'shitwad', 'shitwads',
            'dickwad', 'dickwads',
            'cuntwad', 'cuntwads',
            'asswad', 'asswads',
            'pisswad', 'pisswads',
            'wankwad', 'wankwads',
            'fuckwit', 'fuckwits',
            'shitwit', 'shitwits',
            'dickwit', 'dickwits',
            'cuntwit', 'cuntwits',
            'asswit', 'asswits',
            'pisswit', 'pisswits',
            'wankwit', 'wankwits',
            'fucknut', 'fucknuts',
            'shitnut', 'shitnuts',
            'dicknut', 'dicknuts',
            'cuntnut', 'cuntnuts',
            'assnut', 'assnuts',
            'pissnut', 'pissnuts',
            'wanknut', 'wanknuts',
            'fuckhead', 'fuckheads',
            'shithead', 'shitheads',
            'dickhead', 'dickheads',
            'cunthead', 'cuntheads',
            'asshead', 'assheads',
            'pisshead', 'pissheads',
            'wankhead', 'wankheads',
            'fuckface', 'fuckfaces',
            'shitface', 'shitfaces',
            'dickface', 'dickfaces',
            'cuntface', 'cuntfaces',
            'assface', 'assfaces',
            'pissface', 'pissfaces',
            'wankface', 'wankfaces',
            'fuckbutt', 'fuckbutts',
            'shitbutt', 'shitbutts',
            'dickbutt', 'dickbutts',
            'cuntbutt', 'cuntbutts',
            'assbutt', 'assbutts',
            'pissbutt', 'pissbutts',
            'wankbutt', 'wankbutts',
            'fucktoy', 'fucktoys',
            'shittoy', 'shittoys',
            'dicktoy', 'dicktoys',
            'cunttoy', 'cunttoys',
            'asstoy', 'asstoys',
            'pisstoy', 'pisstoys',
            'wanktoy', 'wanktoys',
            'fuckball', 'fuckballs',
            'shitball', 'shitballs',
            'dickball', 'dickballs',
            'cuntball', 'cuntballs',
            'assball', 'assballs',
            'pissball', 'pissballs',
            'wankball', 'wankballs',
            'fucktard', 'fucktards',
            'shittard', 'shittards',
            'dicktard', 'dicktards',
            'cunttard', 'cunttards',
            'asstard', 'asstards',
            'pisstard', 'pisstards',
            'wanktard', 'wanktards',
            'fuckshit', 'fuckshits',
            'shitfuck', 'shitfucks',
            'dickfuck', 'dickfucks',
            'cuntfuck', 'cuntfucks',
            'assfuck', 'assfucks',
            'pissfuck', 'pissfucks',
            'wankfuck', 'wankfucks',
            'fuckcock', 'fuckcocks',
            'shitcock', 'shitcocks',
            'dickcock', 'dickcocks',
            'cuntcock', 'cuntcocks',
            'asscock', 'asscocks',
            'pisscock', 'pisscocks',
            'wankcock', 'wankcocks',
            'fuckpiss', 'fuckpisses',
            'shitpiss', 'shitpisses',
            'dickpiss', 'dickpisses',
            'cuntpiss', 'cuntpisses',
            'asspiss', 'asspisses',
            'pisspiss', 'pisspisses',
            'wankpiss', 'wankpisses',
            'fuckwank', 'fuckwanks',
            'shitwank', 'shitwanks',
            'dickwank', 'dickwanks',
            'cuntwank', 'cuntwanks',
            'asswank', 'asswanks',
            'pisswank', 'pisswanks',
            'wankwank', 'wankwanks'
        ]
        
        # Regex pattern yaratish (butun so'z sifatida)
        patterns = []
        for word in self.bad_words:
            # So'z boshida va oxirida word boundary
            pattern = r'\b' + re.escape(word) + r'\b'
            patterns.append(pattern)
        
        # Barcha patternlarni birlashtirish
        self.profanity_pattern = re.compile(
            '|'.join(patterns),
            re.IGNORECASE | re.UNICODE
        )
        
        # Simvollarni almashtirish (o'qib bo'lmaydigan qilish uchun)
        self.char_replacements = {
            'а': 'a', 'о': 'o', 'е': 'e', 'р': 'p', 'с': 'c',
            'х': 'x', 'у': 'y', 'к': 'k', 'н': 'h',
            'А': 'A', 'О': 'O', 'Е': 'E', 'Р': 'P', 'С': 'C',
            'Х': 'X', 'У': 'Y', 'К': 'K', 'Н': 'H',
        }
    
    def _normalize_text(self, text: str) -> str:
        """Matnni normalizatsiya qilish"""
        # Shifrlangan belgilarni ochish
        normalized = text
        for cyrillic, latin in self.char_replacements.items():
            normalized = normalized.replace(cyrillic, latin)
        
        # Bo'shliqlarni olib tashlash va kichik harfga o'tkazish
        normalized = normalized.lower()
        
        # Maxsus belgilarni almashtirish
        normalized = re.sub(r'[^\w\s]', '', normalized)
        
        return normalized
    
    def check(self, text: str) -> bool:
        """Matnda so'kinish so'zi bor-yo'qligini tekshirish"""
        if not text:
            return False
        
        # Oddiy tekshirish
        if self.profanity_pattern.search(text):
            return True
        
        # Normalizatsiya qilingan matn bilan tekshirish
        normalized = self._normalize_text(text)
        if self.profanity_pattern.search(normalized):
            return True
        
        # Simvol orasiga qo'yilgan belgilarni tekshirish
        # Masalan: f*u*c*k -> fuck
        cleaned = re.sub(r'[^a-zA-Zа-яА-Я]', '', text.lower())
        if self.profanity_pattern.search(cleaned):
            return True
        
        return False


class AdFilter:
    """Reklama va spamni aniqlash"""
    
    def __init__(self):
        # Reklama patternlari
        self.ad_patterns = [
            # Telegram kanallar/guruhlar linklari (faqat linklar)
            r't\.me/\w+',  # Telegram link
            r'telegram\.me/\w+',
            
            # URL va linklar
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            
            # Reklama kalit so'zlari kombinatsiyasi
            r'(?:купи|купить|продам|продать|скидка|акция|бесплатно|бесплатн|халява)',
            r'(?:sotib|sotaman|sotadi|olaman|oladi|pul|mablag|kredit|taklif)',
            r'(?:buy|sell|discount|sale|free|money|cash|profit|earn|make money|click here)',
            
            # Hashtaglar ko'p bo'lsa (reklama belgisi)
            r'#\w+.*#\w+.*#\w+.*#\w+',
        ]
        
        self.ad_regex = re.compile(
            '|'.join(self.ad_patterns),
            re.IGNORECASE | re.UNICODE
        )
        
        # Minimal xabar uzunligi (qisqa reklama bo'lmasligi uchun)
        self.min_length = 50
        
        # Reklama kalit so'zlari (alohida tekshirish uchun)
        self.ad_keywords = [
            'купи', 'купить', 'продам', 'продать', 'скидка', 'акция',
            'sotib', 'sotaman', 'sotadi', 'taklif', 'pul', 'mablag',
            'buy', 'sell', 'discount', 'sale', 'free money', 'make money'
        ]
    
    def check(self, text: str) -> bool:
        """Matnda reklama bor-yo'qligini tekshirish"""
        if not text or len(text.strip()) < 10:
            return False
        
        text_lower = text.lower()
        
        # URL yoki telegram link tekshirish
        url_match = re.search(
            r'http[s]?://|t\.me/|telegram\.me/',
            text_lower
        )
        
        # Agar URL/telegram link bo'lsa
        if url_match:
            # Va matn qisqa bo'lsa (reklama belgisi)
            if len(text) < self.min_length:
                return True
            
            # Yoki reklama kalit so'zlari bilan birga bo'lsa
            ad_keyword_count = sum(1 for keyword in self.ad_keywords if keyword in text_lower)
            if ad_keyword_count >= 2:
                return True
        
        # Pattern tekshirish
        matches = self.ad_regex.findall(text)
        unique_matches = [m for m in matches if m]
        
        # Agar 3+ pattern mos kelsa, bu reklama
        if len(unique_matches) >= 3:
            return True
        
        # Agar URL va reklama kalit so'zi birga bo'lsa
        if url_match:
            ad_keyword_count = sum(1 for keyword in self.ad_keywords if keyword in text_lower)
            if ad_keyword_count >= 1:
                return True
        
        # Agar takrorlanuvchi simvollar bo'lsa (spam belgisi)
        if re.search(r'(.)\1{15,}', text):
            return True
        
        # Agar katta harflar bilan yozilgan uzun xabar bo'lsa (spam)
        if re.match(r'^[А-ЯA-Z\s\d]{40,}$', text):
            return True
        
        # Ko'p hashtag va reklama so'zi birga bo'lsa
        hashtag_count = len(re.findall(r'#\w+', text))
        if hashtag_count >= 3:
            ad_keyword_count = sum(1 for keyword in self.ad_keywords if keyword in text_lower)
            if ad_keyword_count >= 1:
                return True
        
        return False

