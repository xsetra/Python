#!/usr/bin/env python
# -*- coding: utf-8 -*-
turkce_harfler="İşüğçöÜĞŞÇÖI"
def isim_kisalt_5_harf(isim):
    """Girilen ismin ilk beş harfini ekrana basar"""
    yeni_isim=""
    sayac=0 #sayac kullanıyoruz böylece 5. harfe gelindiğinde döngüden çıkıcaz
    for i in isim:
        if(i in turkce_harfler):
            pass
        else:

            if(sayac==5):
                break
            else:
                yeni_isim+=i
                sayac+=1
    print yeni_isim
in_isim=raw_input("İsminizi Giriniz:")
isim_kisalt_5_harf(isim=in_isim)
