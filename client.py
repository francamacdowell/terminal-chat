#!/usr/bin/env python3
import socket
import threading
import sys


def error(e):
    print(e)
    sys.exit(-1)

try:
    input = raw_input
except NameError:
    pass

if __name__ == "__main__":
        
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        uname = input("Enter user name: ")
    except KeyboardInterrupt:
        error('\nYou choose to exit.')

    ip = '127.0.0.1'

    port = 3333

    try:
        s.connect((ip, port))
    except Exception as e:
        error('Error ocurred: ' + str(e) + '\nTry connecting again later!')

    # sending name to server
    s.send(uname.encode('ascii'))



    client_running = True
    def receive_msg(sock):
        server_down = False
        while client_running and (not server_down):
            try:
                msg = sock.recv(1024).decode('ascii')
                print(msg)
            except:
                error('Server is Down. You are now Disconnected.')


    threading.Thread(target=receive_msg, args=(s,)).start()

    while client_running:

        try:
            temp_msg = input()
        except KeyboardInterrupt:
            error('You choose to exit.')

        msg = uname + '>>' + temp_msg
        if '--quit' in msg:
            clientRunning = False
            s.send('--quit'.encode('ascii'))
        else:
            s.send(msg.encode('ascii'))
