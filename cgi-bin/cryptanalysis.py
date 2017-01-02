#!/usr/bin/env python3
import cgi
import os
import caesar


form = cgi.FieldStorage()
data = form.getfirst("data")
method = form.getfirst("chkMethod")
act = form.getfirst("act")
code_key = form.getfirst("encodeKey")

c = caesar.Caesar(data, code_key)                # создаем объект Caesar для обработки методом Цезаря
t_data = c.transform()                           # трансформируем текст
verifi = c.verifi(code_key)                      # верифицируем входящие данные

if verifi == "данные валидны":
    if method == "caesar":
        if act == "encode":
            res = c.encode(code_key)
        elif act == "decode":
            res = c.decode(code_key)
        elif act == "breaking":
            a = c.breaking()
            code_key = a
            res = c.decode(a)
        else:
            res = "метод в разработке"
    else:
        res = "метод в разработке"
else:
    res = "данные не прошли верификацию, необходимо внести исправления"

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h3>Результат</h3>")
print("<p>данные для анализа: {}</p>".format(data))
print("<p>преобразованные данные: %s </p>" % t_data)
print("<p>выбранный метод: %s </p>" % method)
print("<p>выбранное действие: %s </p>" % act)
print("<p>ключ шифрования: %s </p>" % code_key)
print("<p>верификация данных: %s </p>" % verifi)
print("<p><b><h4>Результат:</h4></b> %s </p>" % res)
print('</body>\n')
print('</html>')