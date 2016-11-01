#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Socket kütüphanesini dahil ediyoruz.
import socket

def Main():
	host = "127.0.0.1"
	port = 5000

	# Python socket örneği oluşturduk
	mySocket = socket.socket()

	# Parametre olarak tuple almak zorunda
	# Socketimizi bağlıyoruz. Belirtilen porta.
	mySocket.bind( (host, port) )

	# Listen 1 ile biz kapatana kadar baglantı acık
	mySocket.listen(1)

	# Clien'in adresini ve baglantisini tutacagız.
	conn, addr = mySocket.accept()

	print ("Connection from: " + str(addr) )

	# Baglantıdan, veri almaya çalısıyoruz
	# Decode ediyoruz. Bu py3 için gerekli
	# Ayrıca bu işlemi döngüye alıyoruz.
	# Bağlantı kapatılmadıkça sunucuda çalıştıracağız.
	# Gelen veriyi Upper ile büyütüyoruz.
	# Ve geriye gönderiyoruz.
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print ("From connected user: " + str(data) )

		data = str(data).upper()

		print ("Sending..: " + str(data) )

		conn.send(data.encode())

	conn.close()

if __name__ == '__main__':
	Main()