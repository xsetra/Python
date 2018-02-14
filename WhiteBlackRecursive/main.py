# -*- coding: utf-8 -*-
# /usr/bin/env python3
import math


def s(sayi, dizi):
    if sayi == 0:
        return 1
    elif sayi == 1:
        return len(dizi)
    else:
        limit = len(dizi) - sayi
        i = 0
        toplam = 0
        for l in range(limit):
            dizi[i] = 0
            dizi[i+1] = 1
            new_dizi = dizi[i+2:]
            toplam += s(sayi-1, new_dizi)
            i += 1
        return toplam


def calc_limit(n):
   if n % 2 == 0:
       return int((n / 2) + 1)
   else:
       return int(math.ceil(n / 2))


if __name__ == '__main__':
   try:
       n = int(input("Number :"))
   except:
       raise TypeError("Number değeri, integer olmalıdır.")
   
   if n <= 0:
       print("N değeri 0 veya daha küçük bir değer olamaz.")
       return

   main = []
   for i in range(n):
       main.append(1)

   limit = calc_limit(n)
   toplam = 0
   for l in range(limit):
       main[0] = 1
       new_main = main[1:]
       toplam += s(l, new_main)
   print(toplam)

