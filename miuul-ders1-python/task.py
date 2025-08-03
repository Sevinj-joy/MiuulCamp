#libraries
import pandas as pd
import numpy as np
import seaborn as sns

#task 1

x = 8
y = 3.2
z  = 8j + 18
a = 'Hello World'
b = True
c = 23 < 22
l=[1,2,3,4]
d={
    "Name": "John",
    "Age": 22,
    "Adress" : "Downtown"
}
t = {"Machine Learning","Data Science"}

s={"Python","Machine Learning","Data Science"}

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(l))
print(type(d))
print(type(t))
print(type(s))

# task 2

text = "The goal is to turn data into information, and information into insight."
words = [word.strip(".,") for word in text.split()]
words_upper = [word.upper() for word in words]
print(words_upper)

#task 3

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.
print(len(lst))

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
print(lst[0])
print(lst[10])

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
sub_list = lst[0:4]
print(sub_list)

# Adım 4: Sekizinci indeksteki elemanı siliniz.
del lst[8]
print(lst)

# Adım 5: Yeni bir eleman ekleyiniz. (Listenin sonuna ekler)
lst.append("X")
print(lst)

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.
lst.insert(8, "N")
print(lst)

#task 4

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adım 1: Key değerlerine erişiniz.
print(dict.keys())

# Adım 2: Value'lara erişiniz.
print(dict.values())

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
dict['Daisy'][1] = 13
print(dict)

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
dict['Ahmet'] = ["Turkey", 24]
print(dict)

# Adım 5: Antonio'yu dictionary'den siliniz.
del dict['Antonio']
print(dict)