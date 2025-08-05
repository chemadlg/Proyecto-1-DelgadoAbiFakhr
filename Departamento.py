class Departamento:
    """
    Representa un departamento del Museo.

    Atributos
    id : int
        Identificador único del departamento.
    nombre : str
        Nombre descriptivo del departamento.
    """

    def __init__(self, id: int, nombre: str) -> None:
        """
        Inicializa una nueva instancia de Departamento.

        Parámetros

        id : int
            Identificador único del departamento.
        nombre : str
            Nombre descriptivo del departamento.
        """
        self.id = id
        self.nombre = nombre

    def show(self) -> None:
        """
        Imprime los atributos una instancia de la clase Departamento.
        """
        print(f"-ID: {self.id}\n-Nombre: {self.nombre}")
