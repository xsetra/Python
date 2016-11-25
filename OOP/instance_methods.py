#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Karakter():
    Karakterler = []

    def __init__(self, nickname, ulus, sinif, ekipman, guc):
        self.Nickname = str(nickname)
        self.Ulus = str(ulus)
        self.Sinif = str(sinif)
        self.Ekipmanlar = []
        self.Gucler = []
        self.Stat = ""

        self.EkipmanEkle(ekipman)
        self.GucEkle(guc)

        self.Karakterler.append(self) #Karakterler listesine kendisini ekliyor.

    def EkipmanEkle(self, ekipman):
        self.Ekipmanlar.append(str(ekipman))
        self.Stat = "Ekipman eklendi."

    def GucEkle(self, guc):
        self.Gucler.append(str(guc))
        self.Stat = "Güç eklendi."

    def GucListele(self):
        temp = "Güçler\n"
        for guc in self.Gucler:
            temp += ">"+guc+"\n"
        return temp

    def EkipmanListele(self):
        temp = "Ekipmanlar\n"
        for item in self.Ekipmanlar:
            temp += ">"+item+"\n"
        return temp

Buyucu = Karakter("abdullah","demasya","buyucu","Asa","Ejder Nidası")

print(Buyucu.GucListele())
print(Buyucu.EkipmanListele())