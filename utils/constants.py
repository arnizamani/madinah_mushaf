# pylint: disable=missing-module-docstring
SPACE            = '\u0020'
HAMZA            = '\u0621'
ALEF_HAMZA_ABOVE = '\u0623'
WAW_HAMZA_ABOVE  = '\u0624'
ALEF_HAMZA_BELOW = '\u0625'
YEH_HAMZA_ABOVE  = '\u0626'
ALEF             = '\u0627'
BEH              = '\u0628'
TEH              = '\u062A'
THEH             = '\u062B'
DAL              = '\u062F'
THAL             = '\u0630'
JEEM             = '\u062C'
HAH              = '\u062D'
KHAH             = '\u062E'
REH              = '\u0631'
ZAIN             = '\u0632'
SEEN             = '\u0633'
SHEEN            = '\u0634'
SAD              = '\u0635'
DAD              = '\u0636'
TAH              = '\u0637'
ZAH              = '\u0638'
AIN              = '\u0639'
GHAIN            = '\u063A'

TATWEEL          = '\u0640'
FEH              = '\u0641'
QAF              = '\u0642'
KAF              = '\u0643'
LAM              = '\u0644'
MEEM             = '\u0645'
NOON             = '\u0646'
HEH              = '\u0647'
WAW              = '\u0648'
ALEF_MAQSURA     = '\u0649'
FATHA            = '\u064E'

KASRA            = '\u0650'
SHADDA           = '\u0651'
MADDA            = '\u0653'
HAMZA_ABOVE      = '\u0654'
HAMZA_BELOW      = '\u0655'

SUP_ALEF         = '\u0670'
YEH              = '\u06CC' # Urdu Yeh (dotless)
END_OF_AYAH      = '\u06DD'
SUKUN            = '\u06E1'
FILLED_DOT_ABOVE = '\u06EC'
NARROW_NO_BREAK_SPACE = '\u202F'

SURAH_WORD = 'سُورَةُ'

SURAH_COUNT = 114
AYAAT_COUNT = 6236
BISMILLAH_COUNT = 112  # One in Fatiha is actullay an Ayah. One missing in Tawba.

BRACKET_START = '\uFD3F'
BRACKET_END   = '\uFD3E'

WESTERN_TO_ARABIC = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
ARABIC_TO_URDU = str.maketrans('٠١٢٣٤٥٦٧٨٩', '۰۱۲۳۴۵۶۷۸۹')

# Letters that combine to the next character
COMBINING_1 = '[' + BEH + TEH + THEH + JEEM + HAH + KHAH + SEEN + SHEEN + SAD + DAD + TAH + ZAH +\
              AIN + GHAIN + FEH + QAF + KAF + LAM + MEEM + NOON + HEH + HAMZA_ABOVE + YEH + ']'
# Letters that combine to the preceding character
COMBINING_2 = '[' + ALEF + BEH + TEH + THEH + JEEM + HAH + KHAH + DAL + THAL + REH + ZAIN +\
              SEEN + SHEEN + SAD + DAD + TAH + ZAH + AIN + GHAIN + FEH + QAF + KAF + LAM + MEEM +\
              NOON + WAW + HEH + YEH + ALEF_HAMZA_ABOVE + WAW_HAMZA_ABOVE + TATWEEL +\
              ALEF_HAMZA_BELOW + ']'

COMBINING_2_MADDA = f'{ALEF_HAMZA_ABOVE}|{ALEF_HAMZA_BELOW}|{WAW_HAMZA_ABOVE}|{YEH_HAMZA_ABOVE}' +\
                    f'|{TATWEEL}{HAMZA_ABOVE}|{JEEM}|{QAF}|{FEH}|{DAD}|{NOON}{SHADDA}' +\
                    f'|{ALEF_MAQSURA}{HAMZA_BELOW}{KASRA}'

NON_COMBINING_1 = '[' + DAL + THAL + REH + ZAIN + WAW + HAMZA + ALEF_HAMZA_ABOVE + ']'
NON_COMBINING_2 = '[' + ALEF + BEH + TEH + THEH + JEEM + HAH + KHAH + DAL + THAL + REH + ZAIN +\
                  SEEN + SHEEN + SAD + DAD + TAH + AIN + GHAIN + FEH + QAF + KAF + LAM + MEEM +\
                  NOON + WAW + HEH + HAMZA + WAW_HAMZA_ABOVE + YEH_HAMZA_ABOVE + YEH +\
                  FILLED_DOT_ABOVE + HAMZA_ABOVE + ']'

FATHA_HIGHALEF_REPLACEMENTS = [
    # Combining
    (f'({COMBINING_1}){FATHA}{SUP_ALEF}({COMBINING_2})',
     f'\\1{FATHA}{TATWEEL}{SUP_ALEF}\\2'),
    # Combining with Shadda
    (f'({COMBINING_1}){SHADDA}{FATHA}{SUP_ALEF}({COMBINING_2})',
     f'\\1{SHADDA}{FATHA}{TATWEEL}{SUP_ALEF}\\2'),
    # Combining with Madda
    (f'({COMBINING_1}){FATHA}{SUP_ALEF}{MADDA}({COMBINING_2_MADDA})',
     f'\\1{FATHA}{TATWEEL}{SUP_ALEF}{MADDA}\\2'),
    # Combining with Shadda+Madda
    (f'({COMBINING_1}){SHADDA}{FATHA}{SUP_ALEF}{MADDA}({COMBINING_2_MADDA})',
     f'\\1{SHADDA}{FATHA}{TATWEEL}{SUP_ALEF}{MADDA}\\2'),
    # Non-combining
    (f'({NON_COMBINING_1}){FATHA}{SUP_ALEF}({NON_COMBINING_2})',
     f'\\1{FATHA}{NARROW_NO_BREAK_SPACE}{SUP_ALEF}\\2'),
    # Non-combining with Shadda
    (f'({NON_COMBINING_1}){SHADDA}{FATHA}{SUP_ALEF}({NON_COMBINING_2})',
     f'\\1{SHADDA}{FATHA}{NARROW_NO_BREAK_SPACE}{SUP_ALEF}\\2'),
    # Non-combining with Madda
    (f'({NON_COMBINING_1}){FATHA}{SUP_ALEF}{MADDA}({NON_COMBINING_2})',
     f'\\1{FATHA}{NARROW_NO_BREAK_SPACE}{SUP_ALEF}{MADDA}\\2'),
]
