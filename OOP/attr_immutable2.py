#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Calisan():
    Personeller = []
    Unvan = ""
    Maas = 0
    Ad = ""
    Soyad = ""

    def BilgiEkle(self, Unvan="", Maas=0, Ad="", Soyad=""):
        """
        Parametre olarak aldığı 4 değeri o anki örnek için doldurur.
        :param Unvan:
        :param Maas:
        :param Ad:
        :param Soyad:
        :return:
        """
        self.Unvan = Unvan
        self.Maas = Maas
        self.Ad = Ad
        self.Soyad = Soyad

        self.Personeller.append(self)

    def BilgiListele(self):
        """
        :return:string
         Geri dönüş değeri olarak, Çalışanın bilgileri döner.
        """
        temp = "Ad:"+self.Ad+\
               "\tSoyad:"+self.Soyad+\
               "\tÜnvan:"+self.Unvan+\
               "\tMaaş:"+str(self.Maas)
        return temp

ahmet = Calisan()
ahmet.BilgiEkle("Memur", 2000, "Ahmet", "SOY")

abdullah = Calisan()
abdullah.BilgiEkle("SE", 2000, "Abdullah", "Caliskan".upper())

print(abdullah.BilgiListele())

print(abdullah.Personeller) # Burada oluşturdugumuz nesnelerin adresleri var