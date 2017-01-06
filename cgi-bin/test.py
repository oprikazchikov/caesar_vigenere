# coding=utf-8
import vigenere

#dic = vigenere.form_dict()
#print(dic)

ec_val = vigenere.encode_val("АБВГЯ")
print(ec_val)

comp = vigenere.comparator("АБВГ", "А")
print(comp)

ec = vigenere.full_encode("АБВГ", "А")
print(ec)