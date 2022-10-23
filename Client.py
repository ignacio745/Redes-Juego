from socket import *



if __name__ == "__main__":
    server_name = '127.0.0.2'
    server_port = 13000

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))

    client_socket.recv(1024)
    
    resultado = 0
    while resultado != "Ganaste" and resultado != "Perdiste":
        origen = int(input("Ingresa la torre origen: "))
        destino = int(input("Ingresa la torre destino: "))
        
        client_socket.send("{0}{1}".format(origen, destino).encode())
        resultado = client_socket.recv(1024).decode()

        if resultado == "-1":
            print("Movimiento ilegal")
        elif resultado == "1":
            print("Movimiento realizado")
        
    print(resultado)