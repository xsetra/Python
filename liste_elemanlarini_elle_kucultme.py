#!/usr/bin/env python
# -*- coding: utf-8 -*-
def liste_lower(g_liste):
	sira=0
	for i in g_liste:
		g_liste[sira]=i.lower()
		sira=sira+1
	return g_liste

liste=["PYTHON","RUBY","PERL"]
liste=liste_lower(liste)
print liste