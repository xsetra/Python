#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Calisan():
    kabiliyetleri = []
    unvani = "Memur"
    maas = 2000
    memleket = ""

ahmet = Calisan()
ayse = Calisan()

ahmet.maas = 2100 # int veri tipi immutable'dır (değiştirilemez)
print(ahmet.maas)
print(ayse.maas)

ahmet.kabiliyetleri.append("Tester") # Listeler mutable bir veri tipi
print(ahmet.kabiliyetleri)
print(ayse.kabiliyetleri) # aynı değişiklikler ayşe de var sebebi kabiliyetleri bir sınıf niteliği
