#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
metin = "tbyksr çsn jücho elu gloglu"
kaynak= "defghijklmnoprstuvyzabc"
hedef = "abcdefghijklmnoprstuvyz"
cevir = string.maketrans(kaynak,hedef)
soncevir = metin.translate(cevir)
print soncevir