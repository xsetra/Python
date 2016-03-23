#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random

class Zar:
    def __init__(self, secim = None):
        self.secim_kontrol(secim)
        self.sonuc = ''
        self.zarDegeri = self.zar_at()
        print('Zar Degeri {}'.format(self.zarDegeri))
        self.zar_kazanim()

    def secim_kontrol(self, secim):
        if secim != 't' or secim != u'ç':
            self.secim_yap()
        else:
            return (self.secim)

    def secim_yap(self):
        self.secim = input('Bir Seçim Yapınız : (t/ç) ')

    def zar_at(self):
        return (random.randint(0,6))
    
    def zar_kazanim(self):
        if (self.zarDegeri % 2 == 0 and self.secim == 'ç') or (self.zarDegeri % 2 != 0 and self.secim == 't'):
            self.sonuc = 'e'
        else:
            self.sonuc = 'h'
            
    @staticmethod
    def kim_kazandi(zar1, zar2):
        if zar1.sonuc == zar2.sonuc:
            print('Kazanan Yok :)')
        
        elif zar1.sonuc == 'e' and zar2.sonuc == 'h':
            print('1. Zar Kazandı.')
        
        else:
            print('2. Zar Kazandı.')

if __name__ == '__main__':
    zar1 = Zar()
    zar2 = Zar()
    Zar.kim_kazandi(zar1, zar2)
else:
    print('Modül aktarım izin verilmez')
