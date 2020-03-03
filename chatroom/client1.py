import socket
import select
import errno
import sys
import threading

Hed_Len=10

name=input("Type UserName that will be shown to other users\n")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address=socket.gethostbyname(socket.gethostname())
Port=15656
client_socket.connect((IP_address, Port))
client_socket.setblocking(False)
username=name.encode('utf-8')
username_header=f"{len(username):<{Hed_Len}}".encode('utf-8')
client_socket.send(username_header+username)


class PrintThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            try:
                username_header=client_socket.recv(Hed_Len)
                if not len(username_header):
                    print("Something bad happend, Connection is closed")
                    sys.exit()
                username_len = int(username_header.decode("utf-8").strip())
                username=client_socket.recv(username_len).decode('utf-8')
                message_header = client_socket.recv(Hed_Len)
                message_len = int(message_header.decode("utf-8").strip())
                message = client_socket.recv(message_len).decode('utf-8')
                print(f"{username}>{message}")
            except BlockingIOError:
                pass

class InputThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        while True:
            try:
                message = input()
                if message:
                    message = message.encode('utf-8')
                    message_header = f"{len(message):<{Hed_Len}}".encode('utf-8')
                    client_socket.send(message_header + message)

            except BlockingIOError:
                pass

try:
        b = InputThread(2,username)
        b.start()
        a = PrintThread(1,username)
        a.start()


except IOError as e:
    if e.errno != errno.EAGAIN and e.errno !=errno.EWOULDBLOCK:
        print("Reading error",str(e))
        sys.exit()
except Exception as e:
    print("General error",str(e))
    sys.exit()