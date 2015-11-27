#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tr_lower(karakter_dizisi):
	""" Fonksiyonumuz türkçe harf içeren karakter dizilerininde küçük harfe çevrilmesini sağlar """
	buyuk_harf={"İ":"i","Ş":"ş","Ü":"ü","Ğ":"ğ","Ç":"ç","Ö":"ö"}
	for harf in buyuk_harf:
		if harf in karakter_dizisi:
			karakter_dizisi=karakter_dizisi.replace(harf,buyuk_harf[harf])
	return karakter_dizisi.lower()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
kelime=raw_input("Bir kelime giriniz >")
kelime=tr_lower(kelime)
print kelime