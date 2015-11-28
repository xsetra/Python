#/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib
site="https://tr.wikipedia.org/wiki/World_Wide_Web"
aranacak_terim="www"
site=urllib.urlopen(site)
site="".join(site)
sonuc=re.search(aranacak_terim,site)
if sonuc:
	print "Aranılan kelime bulundu %s" %sonuc.group()
else:
	print "Aranılan kelime bulunamadı %s" %aranacak_terim
