#! /usr/bin/env python3
# -*- coding: utf-8 -*-

class Asker():
    Rutbe = 'Er'
    Ekipman = ['M4A1','Knife']
    Gucu = 28
    Clan = 'Programmer'

    # print(Rutbe) #Sınıfların içerikleri hemen çalışmaya başlar.
    #Çağrılmaya ihtiyaç duymazlar.

print(Asker.Rutbe) # Sınıf niteliklerine erişim
print(Asker.Gucu)

print('Askerin ekipmanları:')
for item in Asker.Ekipman:
    print(item, end='')
print()

print(Asker.Clan)

