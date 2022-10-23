class ErrorApilar(Exception):
    __disco_apilado: int
    __disco_nuevo: int

    def __init__(self, disco_apilado:int, disco_nuevo:int, *args: object) -> None:
        super().__init__(*args)
        self.__disco_apilado = disco_apilado
        self.__disco_nuevo = disco_nuevo
    

    def __str__(self) -> str:
        return "El disco {0} no se puede apilar sobre el disco {1}".format(self.__disco_nuevo, self.__disco_apilado)
