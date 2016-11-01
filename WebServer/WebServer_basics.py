#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

# Sunucunun çalışacagı 
# ip ve port numarasını parametrelerden alıyoruz

HOST, PORT = sys.argv[1], int(sys.argv[2])
HTTP_Response = """HTTP/1.1 200 OK

Hello, WWW!"""

# Bir socket örneği oluşturuyoruz.
# AF_INET : IPv4 için, AF_INET6 : IPv6 için.
# SOCK_STREAM : Güvenilir veri akışı. Baglantı tabanlı
# SOCK_DGRAM : Bağlantısız karşılık vermek.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Socket seçeneklerini ayarlıyorum.
# Aynı adresi kullanmaya izin ver..
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Socketimizi belirtilen porta baglıyorum.
listen_socket.bind( (HOST,PORT) )

# Socketi dinlemeye alıyorum. biz kapatana kadar.
listen_socket.listen(1)

print("HTTP Server Durumu : ACIK Port : {}".format(PORT))

# Artık socket dinlemede. 
# Tek gereken, baglantıyı kabul etmek.

while True:
	# TCP Baglantısı kabul ediliyor.
	client_conn, client_addr = listen_socket.accept()
	# TCP Baglantısı kuruldu.
	print("> Baglanti Kuruldu FROM: {}".format(client_addr))

	# TCP Baglantısı kurulduguna göre, artık bu TCP socket üzerinden
	# veri aktarımı/paket aktarımı yapılabilir.
	# Kullanıcı bize HTTP Request yapıyor....
	# Requesti ekrana basıyoruz.
	print("> FROM:{}\nHTTP Request : {}".format(client_addr,client_conn.recv(1024).decode()))

	# Requeste karşılık olarak, bir cevap göndermeliyiz.
	client_conn.send(HTTP_Response.encode())
	print("> HTTP Response gönderildi.\nTO: {}\n{}".format(client_addr, HTTP_Response))

	# Client ile aramızdaki baglantıyı kapatıyoruz.
	client_conn.close()

# Socket baglantısını kapatıyoruz.
listen_socket.close()