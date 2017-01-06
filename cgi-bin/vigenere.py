# -*- coding: utf-8 -*-


first = 0
last = 0
for i in range(255, 10000):
    if chr(i) == 'А':
        first = i
    elif chr(i) == 'Я':
        last = i + 1
        break
d = [chr(i) for i in range(first, last)]  #(127)]
dl = len(d)

prepval = lambda val: zip(range(0, len(val)), val)

enc = lambda ch, key: (ch + key) % dl
dec = lambda ch, key: (ch - key + dl) % dl


def vigenere(value, key, func):
    kl = len(key)
    value = prepval(value)
    e = [func(ord(c), ord(key[i % kl])) for (i, c) in value]
    return ''.join([d[c] for c in e])



src = 'АБВГ'
key = 'АБ'

tmp = vigenere(src, key, enc)
print(tmp)