#!/usr/bin/env python3
import cgi
#import cgitb; cgitb.enable(display=0, logdir="/tmp")
import os

form = cgi.FieldStorage()
selYfirst = form.getfirst("selY", "не задано")
selYlist = form.getlist("selY")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>selYfirst: {}</p>".format(selYfirst))
print("<p>selYlist: {}</p>".format(selYlist))
print("""</body>
        </html>""")