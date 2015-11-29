#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,re
cwd=os.getcwd() # bulundugumuz dizini ögreniyoruz.
dosyalar=os.listdir(cwd) # bulundugumuz dizin içindeki dosyaları listeye aldık
var=0 # eğerki hiç dosya bulunmadıysa yok uyarısı için olusturdugum variable
for icerik in dosyalar:
	j=re.match(".*mp3",icerik)
	if j:
		var=1
		print j
if var==0:
	print "MP3 uzantıda dosya yok"