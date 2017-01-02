# coding=utf-8
import caesar


class Vigenere:
    """Метод Виженера"""

    def __init__(self, data="АБВГ ДЕЁЖ"):
        """Инициализация"""
        self.data = data
