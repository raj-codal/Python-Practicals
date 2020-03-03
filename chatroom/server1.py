import socket
import select


Hed_Len=10
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP_address=socket.gethostbyname(socket.gethostname())
Port=15656
server_socket.bind((IP_address, Port))
print("Chat Room is created, Waiting for connection")
server_socket.listen(100)
socket_list=[server_socket]
clients={}
def recieve_message(client_socket):
    try:
        message_header=client_socket.recv(Hed_Len)
        if not len(message_header):
            return False
        mes_len=int(message_header.decode("utf-8").strip())
        return {"header":message_header,"data":client_socket.recv(mes_len)}
    except:
        return False
while True:
    read_socket,_,_error_socket=select.select(socket_list,[],socket_list)
    for notified_socket in read_socket:
        if notified_socket ==server_socket:
            client_socket,clinet_addr=server_socket.accept()
            user=recieve_message(client_socket)
            if user is False:
                continue
            socket_list.append(client_socket)
            clients[client_socket]=user
            print(f"Accepted new connection from {clinet_addr[0]}:{clinet_addr[1]} username:{user['data'].decode('utf-8')}")
        else:
            message=recieve_message(notified_socket)
            if message is False:
                print(f"Bad Message {clients[notified_socket]['data'].decode('utf-8')}")
                socket_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user=clients[notified_socket]
            print(f"Message Sent By {user['data'].decode('utf-8')}:{message['data'].decode('utf-8')}")
            for cs in clients:
                if cs !=notified_socket:
                    cs.send(user['header']+user['data']+message['header']+message['data'])
    for notified_socket in _error_socket:
        socket_list.remove(notified_socket)
        del clients[notified_socket]