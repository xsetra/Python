#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Socket kütüphanesini dahil ediyoruz.
import socket

def Main():
	host = "127.0.0.1"
	port = 5000

	cliSocket = socket.socket()
	cliSocket.connect( (host,port) )

	message = input (" -> ")

	while message != 'q':
		cliSocket.send(message.encode())
		data = cliSocket.recv(1024).decode()

		print ('Received data: ' + str(data))

		message = input (' -> ')

	cliSocket.close()

if __name__ == '__main__':
	Main()