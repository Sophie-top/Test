"""
1 - открыть файл и извлечь обертку
2 - прочитать обертку и сохранить в переменную
3 - все буквы заменить строчными
4- убрать из текста "небуквы"
5 - заменить "ё" на "е"
"""

import re
from collections import Counter

with open (r"source.txt", encoding = "utf-8") as data:
	text = data.read()



text = text.lower()
text = re.sub("ё", "e", text)
edited_text = re.findall(r"[а-яё]+", text)

result = dict(Counter(edited_text).most_common(20))
print (result)