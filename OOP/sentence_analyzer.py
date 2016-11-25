#! /usr/bin/env python3
# -*- coding: utf-8 -*-
sesliHarfler = ['a','e','i','u','o','A','E','I','U','O']

class Cumle:

    def __init__(self, cumle):
        self.Cumle = cumle
        self.sesliSayi = 0
        self.sessizSayi = 0
        self.harfSayi = 0
        self.karakterSayi = 0
        self.boslukSayi = 0

        self.Analysis()

    def Analysis(self):
        for c in self.Cumle:
            if c is None:
                self.boslukSayi += 1
                continue
            if self.HarfMi(c):
                self.harfSayi += 1
                if self.SesliMi(c):
                    self.sesliSayi += 1
                else:
                    self.sessizSayi += 1
            else:
                self.karakterSayi += 1

    def Rapor(self):
        temp = "\"{}\"\n".format(self.Cumle)
        temp += "Cumle Uzunlugu:"+str(len(self.Cumle))+"\n"
        temp += "Sesli Harf:"+str(self.sesliSayi)+"\n"+\
                "Sessiz Harf:"+str(self.sessizSayi)+"\n"+\
                "Harf Sayı:"+str(self.harfSayi)+"\n"+\
                "Karakter Sayı:"+str(self.karakterSayi)+"\n"+\
                "Bosluk Sayı:"+str(self.boslukSayi)+"\n"
        return temp

    def HarfMi(self, h):
        ascii = ord(h)
        if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
            return 1
        return 0

    def SesliMi(self,c):
        if c in sesliHarfler:
            return 1
        return 0

pisi = "Özgürlük şimdi başladı"
slogan = Cumle(pisi)
print(slogan.Rapor())