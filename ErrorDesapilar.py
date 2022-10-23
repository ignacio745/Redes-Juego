class ErrorDesapilar(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    
    def __str__(self):
        return "No se puede desapilar un disco de la torre porque esta vacia"