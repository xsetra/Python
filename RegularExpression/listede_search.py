#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def liste_lower(g_liste):
	""" Bu fonk. gelen listenin elemanlarını küçültür ve geriye yeni liste döndürür."""
	sira=0
	for i in g_liste:
		g_liste[sira]=i.lower()
		sira=sira+1
	return g_liste

liste=["PYTHON","RUBY","PERL"]
liste=liste_lower(liste) # liste elemanlarını küçültüyoruz.
for i in liste:
	bulunan=re.search("ruby",i)
	if(bulunan):
		break
	else:
		pass
print bulunan.group()