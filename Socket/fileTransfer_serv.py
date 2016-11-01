#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys


def writeTOFile(data):
    fp = open("recievedFile.txt", "w")
    fp.write(data)
    fp.close()

HOST, PORT = sys.argv[1], int(sys.argv[2])

trans_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
trans_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
trans_socket.bind((HOST, PORT))
trans_socket.listen(1)

while True:
    cli_conn, cli_addr = trans_socket.accept()

    print("> Baglantı Kuruldu FROM:{}".format(cli_addr))

    print("> Data is receiving FROM:{}".format(cli_addr))

    data = ''
    received = cli_conn.recv(1024).decode()
    while (received):
        data += received
        print (received)
        received = cli_conn.recv(1024).decode()
    writeTOFile(data)
cli_conn.close()
