import re

class Caesar:
    """Метод Цезаря"""

    def __init__(self, data = "АБВГ", key="0"):
        """Инициализация"""
        self.data = data                                        # строка
        self.conv_data = 'Конвертация данных не проводилась'    # преобразованная строка
        #self.key = key                                         # ключ шифрования будем передавать в методы сдвига
        self.dic = self.dic()                                   # словарь русских символов (счет с 0)
        self.endic = self.endic()                               # словарь английских символов (счет с 32)

    def dic(self):
        """Формирование словаря"""
        # Ищем русский алфавит в Unicode
        first = 0
        last = 0
        for i in range(255, 10000):
            if chr(i) == 'А':
                first = i
            elif chr(i) == 'Я':
                last = i+1
                break
        # создаем словарь со всеми буквами алфавита и даем им номера от 0 до 31
        DIC = {chr(x): x - first for x in range(first, last)}
        return DIC

    def endic(self):
        """Словарь английских символов (только для e/d)"""
        # Ищем русский алфавит в Unicode
        first = 0
        last = 0
        for i in range(1, 10000):
            if chr(i) == 'A':
                first = i
            elif chr(i) == 'Z':
                last = i + 1
                break
        # создаем словарь со всеми буквами алфавита и даем им номера от 0 до 25
        DIC = {chr(x): x - first for x in range(first, last)}
        UPDIC = {} # переводим ключи словаря (символы алфавита) в верхний регистр
        for i in DIC:
            UPDIC[i.upper()] = DIC[i]
        return UPDIC

    def transform(self):
        """Преобразование строки"""
        str_data = self.data
        str_data = re.sub(r'\s', '', str_data.upper()) # удаляем пробелы и переводим текст в верхний регистр
        str_data = re.sub(r'Ё', 'Е', str_data) # заменяем ё на е
        str_data = re.sub(r'[!1234567890".,№;%:?*()_+/!@#$%^&*|\=-]', '', str_data) # убираем лишние символы
        conv_data = ""
        # добавляем пробелы после каждого 4-го символа
        for i in range(0, len(str_data)):
            if i % 4 <= 0:
                conv_data = conv_data + str_data[i]+" "
            else:
                conv_data += str_data[i]
        self.conv_data = conv_data
        return conv_data

    def verifi(self, key):
        """Проверка входящих данных"""
        res = ""
        str_data = re.sub(r'\s', '', self.data.upper()) # удаляем пробелы и переводим текст в верхний регистр
        str_data = re.sub(r'[ёЁ]', 'Е', str_data) # заменяем ё на е
        str_data = re.sub(r'[!1234567890".,№;%:?*()_+/!@#$%^&*|\=-]', '', str_data) # убираем лишние символы
        tkey = re.sub(r'-', '', key) # т.к. строка может содержать "-" удаляем его перед проверкой
        if not tkey.isdigit():
            res += "ключ должен состоять только из цифр"
        #elif not str_data.isalpha():
        #    res += "строка должна состоять только из текста"
        elif re.search(r'[1234567890]', str_data):
           res += "допустим только русский или английский алфавит"
        else:
            res = "данные валидны"
        return res

    def encode(self, key):
        """Шифрование"""
        e_string = ""
        # если ключ отрицательный - задаем обратное направление (шифруем зеркально)
        if int(key) < 0:
            ikey = 32 + int(key)
        else:
            ikey = int(key)

        for i in self.conv_data:
            #if i not in self.dic:  # если символа нет в словарях (рус + англ) оставляем как есть
            #    e_string += i
            #    continue
            if i in self.dic:
                ch = self.dic[i] + ikey
                if ch > 31:  # букв в словаре 32, счет с 0
                    ch = ch - 32
                #e_string += '|' + str(ch) + '|'
                e_string += self.get_key(self.dic, ch)
            if i in self.endic:
                ch = self.endic[i] + ikey
                if ch > 25:  # букв в словаре 26, счет с 0
                    ch = ch - 26
                #e_string += '|' + str(ch) + '|'
                e_string += self.get_key(self.endic, ch)
        return e_string

    def decode(self, key):
        """Расшифрование"""
        e_string = ""
        # если ключ отрицательный - задаем обратное направление (расшифруем зеркально)
        if int(key) < 0:
            ikey = 32 + int(key)
        else:
            ikey = int(key)
        ikey = int(key)

        # словари
        ru = self.dic      # рус
        eng = self.endic    # англ

        for i in self.conv_data:
            if i not in self.dic:  # если символа нет в словаре оставляем как есть
                e_string += i
                continue
            ch = self.dic[i] - ikey
            if ch < 0:
                ch = ch + 32 # букв в словаре 32, счет с 0
            #e_string += '|' + str(ch) + '|'
            e_string += self.get_key(self.dic, ch)
        return e_string

    def get_key(self, dic, val):
        '''Получение ключа по значению словаря'''
        for i in dic.items():
            if val in i:
                return i[0]

    # ---------------------------------Взлом---------------------------------------

    def breaking(self):
        """Взлом"""
        const_frq = {"А":0.0751, "Б":0.0175, "В":0.0453, "Г":0.0180, "Д":0.0302, "Е":0.0877,
                     "Ж":0.0097, "З":0.0175, "И":0.0744, "Й":0.0118, "К":0.0337, "Л":0.0420,
                     "М":0.0312, "Н":0.0645, "О":0.1101, "П":0.0280, "Р":0.0477, "С":0.0550,
                     "Т":0.0649, "У":0.0248, "Ф":0.0019, "Х":0.0107, "Ц":0.0045, "Ч":0.0149,
                     "Ш":0.0068, "Щ":0.0045, "Ъ":0.0101, "Ы":0.0197, "Ь":0.0079, "Э":0.0032,
                     "Ю":0.0073, "Я":0.0212} # Частоты встречаемости в алфавите

        #const_frq = {"А":0.062, "Б":0.014, "В":0.038, "Г":0.013, "Д":0.025, "Е":0.072,
        #             "Ж":0.007, "З":0.016, "И":0.062, "Й":0.010, "К":0.028, "Л":0.035,
        #             "М":0.026, "Н":0.053, "О":0.090, "П":0.023, "Р":0.040, "С":0.045,
        #             "Т":0.053, "У":0.021, "Ф":0.002, "Х":0.009, "Ц":0.003, "Ч":0.023,
        #             "Ш":0.006, "Щ":0.003, "Ъ":0.014, "Ы":0.016, "Ь":0.014, "Э":0.003,
        #             "Ю":0.006, "Я":0.018} # Частоты встречаемости в алфавите

        temp_out = {}                        # переменная для расчета минимального МНК
        temp_in = 0                          # переменная для расчета МНК строки
        str_data = ""                        # переменная для перебора строки
        res = 0
        i = 0
        for i in range(0, 32):               # перебираем каждый случай сдвига
            str_data = re.sub(r'\s', '', self.data.upper())  # удаляем пробелы базовой строки и переводим текст в верхний регистр
            str_data = re.sub(r'[ёЁ]}', 'Е', str_data)  # заменяем ё на е
            str_data = re.sub(r'[!1234567890"№;%:?*()_+/!@#$%^&*|\=-]', '', str_data)  # убираем лишние символы
            str_data = self.shift_str(str_data, i)     # сдвигаем строку на i
            frq = self.avgchr(str_data)      # получаем частоты сдвинутой строки
            keys = const_frq.keys()
            for j in frq:              # перебираем const_frq
                #if frq.get[j] in keys:  # если буква присутствует в частотах сдвинутой строки
                if frq.get(j) == None:
                    continue
                temp_in += (const_frq.get(j) - frq.get(j))**2
            temp_out[i] = temp_in
            temp_in = 0
        res = 0
        temp_min = temp_out[0]
        for i in range(1, 31):
            if temp_min < temp_out[i]:
                temp_min = temp_min
            else:
                temp_min = temp_out[i]
                res = i
        res = 32 - res
        return res

    def avgchr(self, data):
        """Расчет среднего значения вхождений"""
        res = {}                                        # словарь {А:0.7, Б:0.2, ...}
        n = 0
        temp = ""
        for i in data:  # перебираем строку
            if i in temp:   # если символ уже обработан - пропускаем
                continue
            res[i] = self.countchr(i, data) / len(data) # считаем кол-во вхождений и делим на длинну строки
            temp += i                                           # пишем букву для учета в след итерации
        return res

    def countchr(self, ch, data):
        """Подсчет символов в строке"""
        count = 0
        for i in data:          # проходим по всей строке
            if ch in i:         # если символ входит
                count += 1      # то считаем
        return count

    def min_mnk(self, v1, v2):
        if v1 <= v2:
            return v1
        else:
            return v2

#---- пришлось продублировать метод encode и юзать передаваемую строку-------

    def shift_str(self, str, key):
        """Сдвиг строки"""
        e_string = ""
        for i in str:
            if i not in self.dic:  # если символа нет в словаре оставляем как есть
                e_string += i
                continue
            ch = self.dic[i] + key
            if ch > 31:  # букв в алфавите 32 (у нас счет с нуля)
                ch = ch - 32
            # e_string += '|' + str(ch) + '|'
            e_string += self.get_key2(self.dic, ch)
        return e_string


    def get_key2(self, dic, val):
        '''Получение ключа по значению словаря'''
        for i in dic.items():
            if val in i:
                return i[0]