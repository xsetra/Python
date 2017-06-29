#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Oyuncu:
    def __init__(self, isim):
        self.isim = isim
        self.rutbe = ""
        self.guc = 0

    def hareket_et(self):
        return "Hareket ediliyor..."

    def puan_kazan(self):
        return "Puan kazanılıyor..."


class Asker(Oyuncu):
    def __init__(self, isim):
        super().__init__(isim)
        self.guc = 75

    def hareket_et(self):
        return "Overrided Method"


class Manager(Oyuncu):
    pass


o = Oyuncu("oyuncu")
a = Asker("asker")
print(a.hareket_et())
print(a.guc)

print(o.guc)
