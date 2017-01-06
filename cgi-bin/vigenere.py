# -*- coding: utf-8 -*-
import re


class Vigenere:
    def __init__(self):
        """Инициализация"""
        first = 0
        last = 0
        for i in range(255, 10000):
            if chr(i) == 'А':
                first = i
            elif chr(i) == 'Я':
                last = i + 1
                break
        self.d = [chr(i) for i in range(first, last)]  # (127)]
        self.dl = len(self.d)
        self.prepval = lambda val: zip(range(0, len(val)), val)

        self.enc = lambda ch, key: (ch + key) % self.dl
        self.dec = lambda ch, key: (ch - key + self.dl) % self.dl

    def transform(self, data):
        """Преобразование строки"""
        str_data = re.sub(r'\s', '', data.upper())  # удаляем пробелы и переводим текст в верхний регистр
        str_data = re.sub(r'Ё', 'Е', str_data)  # заменяем ё на е
        str_data = re.sub(r'[!1234567890".,№;%:?*()_+/!@#$%^&*|\=-]', '', str_data)  # убираем лишние символы
        return str_data


    def verifi(self, data, key):
        """Проверка входящих данных"""
        res = ""
        str_data = re.sub(r'\s', '', data.upper())  # удаляем пробелы и переводим текст в верхний регистр
        str_data = re.sub(r'[ёЁ]', 'Е', str_data)  # заменяем ё на е
        str_data = re.sub(r'[!1234567890".,№;%:?*()_+/!@#$%^&*|\=-]', '', str_data)  # убираем лишние символы
        if re.search(r'[a-zA-Z1234567890]', str_data):
            res += "в тексте допустим только русский алфавит "
        elif re.search(r'[a-zA-Z1234567890]', key):
            res += "в ключе допустим только русский алфавит "
        else:
            res = "данные валидны"
        return res

    def vigenere(self, value, key, func):
        kl = len(key)
        value = self.prepval(value)
        e = [func(ord(c), ord(key[i % kl])) for (i, c) in value]
        res = ''.join([self.d[c] for c in e])
        # добавляем пробелы после каждого 4-го символа
        conv_data = ''
        for i in range(0, len(res)):
            if i % 4 <= 0:
                conv_data = conv_data + res[i] + " "
            else:
                conv_data += res[i]
        return conv_data

