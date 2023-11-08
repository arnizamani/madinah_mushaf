# pylint: disable=missing-module-docstring
SPACE  = '\u0020'
BEH    = '\u0628'
KASRA  = '\u0650'
SHADDA = '\u0651'
END_OF_AYAH = '\u06DD'

SURAH_WORD = 'سُورَةُ'

SURAH_COUNT = 114
AYAAT_COUNT = 6236
BISMILLAH_COUNT = 112  # One in Fatiha is actullay an Ayah. One missing in Tawba.

BRACKET_START = '\uFD3F'
BRACKET_END   = '\uFD3E'

WESTERN_TO_ARABIC = str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
URDU_TO_ARABIC = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '٠١٢٣٤٥٦٧٨٩')
