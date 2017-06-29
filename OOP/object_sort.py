#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Kelime():
    def __init__(self, sira, icerik):
        self.index = sira
        self.icerik = icerik

liste = []

k2 = Kelime(2,"iki")
k1 = Kelime(1,"bir")
k0 = Kelime(0,"sıfır")

liste.append(k2)
liste.append(k0)
liste.append(k1)


sirali = sorted(liste, key=lambda sirala2: sirala2.index)
print(sirali[0].icerik)
