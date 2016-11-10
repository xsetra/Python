#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys

class DosyaYoneticisi():
    curr_dir = ''           # Current Directory
    directory_cont = ()     # Directory Content : directories, files, etc.
    command = ['']
    command_income = ''

    def __init__( self, dizin=os.getcwd() ):
        self.curr_dir = dizin
        self.Listele()

    def DizinDegistir(self, dizin):
        self.curr_dir = dizin

    def __DirFileList(g_liste):
        buffer = ''
        for i in g_liste[0]:
            buffer += '\t\t'+i
        return buffer

    def Listele(self):
        print ('******************************************')
        yol = ''
        dizin = []
        dosya = []
        for yol , dizin , dosya in os.walk(self.curr_dir):
            break
        self.directory_cont = dizin + dosya
        print("Content of '{}' ".format(yol))
        print('\tDirectories')
        for n,c in enumerate(self.directory_cont):
            if n == len(dizin):
                print('\tFiles')
            print('\t\t',n,c)

        self.Menu()
        

    def Menu(self):
        print('--Change Directory : cd [dir_no]')
        print('--Delete File      : del [file_no]')
        print('--Read File        : read [file_no]')
        print('--Add to File      : add [file_no]')
        print('--List Content     : list')
        self.Prompt()


    def Prompt(self):
        self.command = []
        self.command_income = input('>>>')
        self.command.append('')
        com_sayac = 0
        for i in self.command_income:
            if i == ' ':
                self.command.append('')
                com_sayac += 1
                continue
            self.command[com_sayac] += i
        self.Decider()

    def Decider(self):

        if self.command[0] == 'list':
            self.Listele()

        elif self.command[0] == 'del':
            procOnFile = Dosya(self.curr_dir, self.directory_cont[ int(self.command[1]) ])
            procOnFile.Sil()
            print(procOnFile.Stat)

        elif self.command[0] == 'read':
            procOnFile = Dosya(self.curr_dir, self.directory_cont[int(self.command[1])])
            procOnFile.Oku()
            print(procOnFile.Stat)

        self.Prompt()




''' class Logger():
    defaultPath = '/var/log/abdullah/dosya_yoneticisi/'
    os.mkdir(defaultPath)

    logFile = Dosya()
    logFile.dosyaPath = defaultPath
    logFile.dosyaAd = 'fileManager.log'
'''


class Dosya():
    Path = ''      # File path
    Ad = ''        # File name
    Full = ''      # File path + File name
    Stat = ''       # Result of process or warning message

    def __init__(self, Path='', Ad=''):
        self.Path = Path
        self.Ad = Ad
        self.Full = self.Path + '/' + self.Ad

    def Ekle(self, content):
        ''' Dosyayı append modunda açıp, parametre olarak gönderilmiş olan content
            değişkenini dosyaya yazar ve Stat değişkenine durumu basar ve dosyayı kapatır
        '''
        fp = open(self.Full, 'a')
        result = fp.write(content)
        if result != 0:
            self.Stat = 'İçerik başarıyla eklendi.'
        else:
            self.Stat = 'İçerik ekleme esnasında hata ile karşılaşıldı.\n'+result
        fp.close()

    def Sil(self):
        result = os.remove(self.Full)
        if result == None:
            # Dosya silindi.
            self.Stat = 'Dosya başarılı bir şekilde silindi.'
        else:
            self.Stat = 'Dosya silinemedi.\n'+result

    def Oku(self):
        fp = open(self.Full, 'r')
        self.Stat = fp.read()
        fp.close()


dosyaci = DosyaYoneticisi()




