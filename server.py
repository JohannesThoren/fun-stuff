import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 25565))

sock.listen(1)
client, addr = sock.accept()
print(f"client connected from {addr}")


def recv(client):
    while True:
        data = client.recv(2048)
        if data == b'':
            client.close()
        else:
            print(f"target output : {data.decode()}\n")

def inp(client):
    print("input ready")

    while True:
        server_in = input("")
        client.send(server_in.encode())


recv_t = threading.Thread(target=recv, args=(client,))
inp_t = threading.Thread(target=inp, args=(client,))

recv_t.start()
inp_t.start()