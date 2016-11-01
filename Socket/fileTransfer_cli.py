#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys


def sizeofFile(file_name):
    dosya = open(file_name, "rb")

    dosya.close()

RHOST, RPORT = sys.argv[1], int(sys.argv[2])
FILE = sys.argv[3]

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect((RHOST, RPORT))

fp = open(FILE, "rb")
satirlar = fp.readlines()

for i in range(len(satirlar)):
    cli_sock.send(satirlar[i].encode())
fp.close()
cli_sock.shutdown(socket.SHUT_WR)
cli_sock.close()
