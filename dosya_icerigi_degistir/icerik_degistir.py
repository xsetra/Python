#!/usr/bin/env python
# -*- coding: utf-8 -*-

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Functions<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

def icerik_degistir(dosyaAdi,degisikliklerSozluk):
    """Bu fonksiyon dosyanın içini okur ve gelen listede arama yapar ve buldugu index te değişiklik yapıp dosyaya yazar"""
    dosya=open(dosyaAdi)
    icerik=dosya.readlines()
    dosya.close()
    sayac=0
    for satirlar in icerik:#satirlarımızı çekiyoruz
        for degiskenler in degisikliklerSozluk.keys():#aranan degiskenleri cekiyoruz
            if degiskenler in satirlar:#aranan degişken o satırda varmı
                icerik[sayac]=degiskenler+"\""+degisikliklerSozluk[degiskenler]+"\";\n" #iceriğimiz liste oldugu için onun içine anahtarımızın
                # sahip oldugu değeri yazıyoruz. \" kaçışı dizisi ile değişkenin değerini string hale geçiiriyoruz. bu php için
            else:
                pass
        sayac+=1 # satır sayımızı bilmek adına degiştiriyoruz
    dosya=open(dosyaAdi,"w")
    dosya.writelines(icerik)
    print "Değişiklikler tamamlandı"
    dosya.close()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Main Program>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

import os
degisiklik_dosyasi=raw_input("Dosyanın ismini giriniz:")
if os.path.exists(degisiklik_dosyasi):
    degisiklikler={}
    while True:
        degisken=raw_input("Degişkenin Adını giriniz:")
        degisken="$"+degisken+"=" # değişken ismini $host= kalıbına soktuk. böylece atama işlemi olan yerlerde değişklik yapıcaz Örnegin;
        # mysql connect fonksiyonunda da geçiyor olabilir
        deger=raw_input("Değişkenin Değerini giriniz:")
        degisiklikler[degisken]=deger # sozlüge ekleme yaptık
        tekrar=raw_input("Tekrar? (e/h):")
        if tekrar=="e":
            pass
        else:
            break
    icerik_degistir(degisiklik_dosyasi,degisiklikler)
else:
    print "Dosya Bulunamadı"