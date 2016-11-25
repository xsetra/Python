#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Calisan():
    Personeller = []
    # Sınıf nitelikleri

    def __init__(self):
        # Örnek nitelikleri
        self.Kabiliyetler = []
        self.Ad = ""
        self.Soyad = ""
        self.Maas = 0
        self.Unvan = ""

abdullah = Calisan()

abdullah.Ad = "Abdullah"
abdullah.Soyad = "ÇALIŞKAN"

abdullah.Kabiliyetler.append("Linux")
abdullah.Kabiliyetler.append("Python")

Calisan.Personeller.append(abdullah)