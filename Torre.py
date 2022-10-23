import numpy as np

from ErrorApilar import ErrorApilar
from ErrorDesapilar import ErrorDesapilar

class Torre:
    __discos: np.ndarray
    __tope: int
    __cantidad: int


    def __init__(self, cant_discos:int) -> None:
        self.__discos = np.empty(cant_discos, dtype=int)
        self.__discos.fill(-1)
        self.__tope = cant_discos
        self.__cantidad = 0
    
    def apilar_disco(self, disco:int):
        if not self.__cantidad < self.__tope:
            raise OverflowError("La torre no admite mas de {0} discos".format(self.__tope))

        if (not self.__cantidad == 0) and (not self.__discos[self.__cantidad-1] > disco):
            raise ErrorApilar(self.__discos[self.__cantidad-1], disco)

        self.__discos[self.__cantidad] = disco
        self.__cantidad += 1
    

    def desapilar_disco(self) -> int:
        if self.__cantidad == 0:
            raise ErrorDesapilar()
        
        self.__cantidad -= 1

        return self.__discos[self.__cantidad]
    
    def altura(self) -> int:
        return self.__cantidad