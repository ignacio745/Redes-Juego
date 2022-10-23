from ErrorApilar import ErrorApilar
from ErrorDesapilar import ErrorDesapilar
from Torre import Torre

class Juego:
    __torres: list[Torre]
    __cant_discos: int

    def __init__(self, cant_discos:int) -> None:
        self.__cant_discos = cant_discos
        self.__torres = [Torre(cant_discos) for i in range(3)]
        for i in range(cant_discos):
            self.__torres[0].apilar_disco(cant_discos-i)
    

    def mover_disco(self, ts:int, td:int):
        try:
            disco = self.__torres[ts].desapilar_disco()
            self.__torres[td].apilar_disco(disco)

        except ErrorDesapilar as movimiento_ilegal:
            print(movimiento_ilegal)

        except ErrorApilar as movimiento_ilegal:
            print(movimiento_ilegal)
            self.__torres[ts].apilar_disco(disco)
            return -1

        except OverflowError as desbordamiento:
            print(desbordamiento)
            return -1

        else:
            return 1
    
    def ganado(self):
        return self.__torres[2].altura() == self.__cant_discos