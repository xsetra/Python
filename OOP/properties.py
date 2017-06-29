#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Ogrenci:
    def __init__(self):
        self._not = 1
        self.Ad = "A"

    @property
    def Not(self):
        return self._not

    @Not.setter
    def Not(self, not_val):
        self._not = not_val

apo = Ogrenci()
apo.Not = 48
print(apo.Not)
