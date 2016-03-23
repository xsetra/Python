#!/usr/bin/env python
# -*- coding: utf-8 -*-
sesli_harfler="aueioöüı"
kelime=input("Bir kelime giriniz:")
sayac=0
for harf in kelime:
    if harf in sesli_harfler:
       sayac+=1
print("Sayac degeri: %d" %(sayac))
