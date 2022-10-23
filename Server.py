import threading
from socket import *

from Juego import Juego


def mover(socket_p:socket, juego_p:Juego, otro_juego_p:Juego):
    movimiento = socket_p.recv(1024).decode()
    origen = int(movimiento[0])
    destino = int(movimiento[1])
    resultado = juego_p.mover_disco(origen-1, destino-1)
    if not juego_p.ganado() and not otro_juego_p.ganado():
        socket_p.send("{0}".format(resultado).encode())





def jugar(socket_p1:socket, socket_p2:socket):
    juego_p1 = Juego(3)
    juego_p2 = Juego(3)
    mover_p1 = threading.Thread(target=mover, args=(socket_p1, juego_p1, juego_p2))
    mover_p1.start()
    mover_p2 = threading.Thread(target=mover, args=(socket_p2, juego_p2, juego_p1))
    mover_p2.start()
    while not (juego_p1.ganado() or juego_p2.ganado()):
        if not mover_p1.is_alive():
            mover_p1 = threading.Thread(target=mover, args=(socket_p1, juego_p1, juego_p2))
            mover_p1.start()
        if not mover_p2.is_alive():
            mover_p2 = threading.Thread(target=mover, args=(socket_p2, juego_p2, juego_p1))
            mover_p2.start()
    print("Juego terminado")

    if juego_p1.ganado():
        socket_p1.send("Ganaste".encode())
        socket_p2.send("Perdiste".encode())
    else:
        socket_p2.send("Ganaste".encode())
        socket_p1.send("Perdiste".encode())


    




if __name__ == "__main__":
    server_name = '127.0.0.2'
    server_port = 13000

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    server_socket.bind((server_name, server_port))
    server_socket.listen(1)

    print("El servidor está listo para recibir")

    jugadores:list[socket] = []

    while len(jugadores) < 2:
        
        un_jugador, addr = server_socket.accept()
        jugadores.append(un_jugador)
    

    jugadores[0].send("Empieza".encode())
    jugadores[1].send("Empieza".encode())
    
    jugar(jugadores[0], jugadores[1])