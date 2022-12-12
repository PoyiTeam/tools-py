from PySide6.QtCore import QLocale


current_locale = QLocale()
print(current_locale)

eng_locale = QLocale(QLocale.English)
print(eng_locale)

chs_locale = QLocale(QLocale.Chinese)
print(chs_locale)

cht_locale = QLocale(QLocale.Chinese, QLocale.TraditionalChineseScript, QLocale.Taiwan)
print(cht_locale)
