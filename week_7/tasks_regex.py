'''Напишите скрипт, который извлекает все хештеги (например, #python) из данного текста.
# Вы можете использовать регулярные выражения, чтобы найти все вхождения хештегов.'''

import re

text_1 = "esfv m sdfm kdsv noef #55dml#fmkfd #python dgndsf@dlmf r# odm lksdv #sfsfj dlm kfds#odf__"

result_1 = re.findall(r"#\w+", text_1)

print(result_1)

'''Откройте текстовый файл для чтения.Прочитайте содержимое файла и сохраните его в
строковой переменной.
Напишите регулярное выражение, которое ищет и извлекает электронные адреса из текста.Используйте модуль
re для выполнения поиска с помощью регулярного выражения.Сохраните найденные адреса в отдельный
файл или выведите их на экран.'''


file = open("text.txt", "r")

# file.write("Mumbai :- Ms.Geeta k, Capt.G.Dasgupta Office No.5 Govar Mansion, 91 Mint Road Fort,\n"
#            "Mumbai 400001 022-27711012 / 022-22620092 pmtri@vsnl.net / pmsmumbai@vsnl.net")
# file.close()

file_text = file.read()

result_2 = re.findall(r"[+0-9A-z._-]+@[A-z.]+", file_text)

print(result_2)