# coding=utf-8

from tkinter import *
import caesar
import vigenere


# ------------------------ Обработка -------------------------------

def event_run(event):
    res_method = method.get()
    res_act = act.get()
    res_key = key.get()
    res_text_in = text_in.get(1.0, END)
    text_out.delete(1.0, END)
    c = caesar.Caesar(res_text_in, res_key)  # создаем объект Caesar для обработки методом Цезаря
    c.transform()  # выполняем трансформацию по Цезарю (особенность реализации(костыль))
    v = vigenere.Vigenere()  # создаем объект Vigenere для обработки методом Виженера
    t_data = v.transform(res_text_in)  # трансформируем текст для Виженера (отдельная процедура трансформаии,
    # т.к. разбивать по 4 символа нужно после обработки (особенность реализации))
    # проводим верификацию входящих данных
    if res_method == 0:  # если метод Цезаря
        verifi = c.verifi(res_key)  # верификация по Цезарю (ключ только цифры и т.д.)
    else:  # евли метод Виженера
        verifi = v.verifi(t_data, res_key)
    if verifi == "данные валидны":
        if res_method == 0:  # Если шифр Цезаря
            if res_act == 0:  # Если Шифрование
                res = c.encode(res_key)
            elif res_act == 1:  # Если Расшифрование
                res = c.decode(res_key)
            elif res_act == 2:  # Если Взлом
                a = c.breaking()  # Получаем ключ
                res = c.decode(a)  # Проводим расшифрование с взломанным ключом
                res = "Ключ шифрования:" + str(a) + '\n' + res
                key.delete(0, END)
                key.insert(END, a)
            else:
                res = "метод в разработке"
        else:
            if res_act == 0:  # Если Шифрование
                res = v.vigenere(t_data, res_key, v.enc)
            elif res_act == 1:  # Если Расшифрование
                res = v.vigenere(t_data, res_key, v.dec)
            else:
                res = "метод в разработке"
    else:
        res = "данные не прошли верификацию, необходимо внести исправления " + verifi
    # Выводим результат
    text_out.insert(END, res)


# ------------------------ Конструктор формы ------------------------------
root = Tk()
root.title = "Криптоанализ"
fra_option = Frame(root)
# Построение элементов окна
lab_in = Label(root, text="Входящие данные", font="Arial 9")
lab_out = Label(root, text="Результат", font="Arial 9")
lab_method = Label(fra_option, text="Метод:")
lab_key = Label(fra_option, text="Ключ шифрования:")
lab_act = Label(fra_option, text="Действие:")
text_in = Text(root, width=40, font="Arial 9", wrap=WORD)  # текст вход
text_out = Text(root, width=40, font="Arial 9", wrap=WORD)  # текст выход
key = Entry(fra_option, width=20, bd=3)
key.insert(END, "0")
run = Button(fra_option, text="Выполнить")  # Кнопка запуска
run.bind('<Button-1>', event_run)
# радиокнопки метода
method = IntVar()
method.set(0)  # по умолчанию Метод Цезаря
meth0 = Radiobutton(fra_option, text="Метод Цезаря", variable=method, value=0)
meth1 = Radiobutton(fra_option, text="Метод Виженера", variable=method, value=1)
# радиокнопки ltqcndbz
act = IntVar()
act.set(0)  # по умолчанию Метод Цезаря
act0 = Radiobutton(fra_option, text="Шифровать", variable=act, value=0)
act1 = Radiobutton(fra_option, text="Расшифровать", variable=act, value=1)
act2 = Radiobutton(fra_option, text="Взломать", variable=act, value=2)

# Размещение
lab_in.grid(row=2, column=0)
lab_out.grid(row=2, column=2)
text_in.grid(row=3, column=0)
text_out.grid(row=3, column=2)
fra_option.grid(row=3, column=1)
lab_method.pack()
meth0.pack()
meth1.pack()
lab_key.pack()
key.pack()
lab_act.pack()
act0.pack()
act1.pack()
act2.pack()

run.pack(side="bottom")

root.mainloop()
