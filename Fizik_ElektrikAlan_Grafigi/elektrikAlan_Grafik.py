#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def ElektrikAlan(icCap, disCap, yariCap, epsilon, blok, ro=1):
    """ RO sabit. A iç çap, B dış çap. B - A olucak. Epsilon Sabit """
    ea = 0.0
    if blok==2:
        ea = ro * ( (yariCap ** 3) - (icCap ** 3) )
        ea = ea / ( 3 * epsilon * (yariCap ** 2) )
    elif blok==1:
        print "Sabit Grafik çiz"
    elif blok==3:
        ea = ro * ( (disCap ** 3) - (icCap ** 3) )
        ea = ea / ( 3 * epsilon * (yariCap**2) )
    else:
        print "Zero"
    return ea


epsilon = 8.85 / (10 ** 12)

iccap = float(raw_input("İç Çapı Giriniz (a) :"))
discap = float(raw_input("Dış Çapı Giriniz (b):"))
yaricap = float(raw_input("Yarı Çapı giriniz(r):"))

#S1 grafik alanı çiz.
x1 = np.arange(0,iccap,0.1)
y1 = []
mutlakR = iccap
noktaSayisi = mutlakR / 0.1
for i in range(0, int(noktaSayisi)):
    y1.append(0)

plt.ylabel('Elektrik Alan')
plt.xlabel('Yari Cap')
plt.plot(x1,y1,'bo',label='S1')

#S2 grafik alanı çiz.
x2 = np.arange(iccap,discap,0.1)
y2 = []
mutlakR = discap - iccap
noktaSayisi = mutlakR / 0.1
deger = int(noktaSayisi) - 1 
for i in range(0,int(noktaSayisi)):
    y2.append(ElektrikAlan(iccap, discap, x2[i], epsilon, blok=2))

plt.plot(x2,y2,'bo',label='S2')

#S3 Grafik alanı çiz
x3 = np.arange(discap,yaricap,0.1)
y3 = []
mutlakR = yaricap - discap
noktaSayisi = mutlakR / 0.1
for i in range(0, int(noktaSayisi)):
    y3.append(ElektrikAlan(iccap, discap, x3[i], epsilon, blok=3))
print y3[int(noktaSayisi)-1]
print "10 daki deger: "
print y2[int(deger)]
plt.plot(x3,y3,'bo',label='S3')
plt.show()
