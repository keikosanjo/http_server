#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from lucky_server_method import Method
import urllib

# サーバー側
host = socket.gethostbyname('IP address')
port = 8080

# ソケット作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ソケットにアドレスをbind
sock.bind((host, port))
# サーバーを有効にして接続受付
sock.listen(1)

while True:
    # 接続受付
    (client_sock, client_addr) = sock.accept()
    # ソケットからデータを受信し、結果を bytes オブジェクトで返す.値はmax値
    receive = client_sock.recv(1024)
    print "受け取ったもの： %s " % receive
    receive_list = receive.splitlines()
    status_line_list = receive_list[0].split(" ")
    url = status_line_list[1].strip('/')
    
    opener = urllib.FancyURLopener({})
    f = opener.open(url)
    msg = f.read()

    method = Method(url, msg)
    response = method.get()

    print " %s " % response
    client_sock.send("%s \n\n" % response)
    f.close()

client_sock.close()

sock.close()
