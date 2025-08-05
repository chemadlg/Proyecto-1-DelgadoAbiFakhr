class Autor:
    """
    Representa un autor asociado a una obra del Museo.

    Atributos
    nombre : str
        Nombre completo del autor.
    nacionalidad : str
        Nacionalidad declarada.
    nacimiento : int
        Año/fecha de nacimiento.
    muerte : int
        Año/fecha de muerte.
    """

    def __init__(self,nombre,nacionalidad,nacimiento, muerte):
        """
        Inicializa una nueva instancia de la clase Autor.

        Parámetros
        nombre : str
            Nombre completo del autor.
        nacionalidad : str
            Nacionalidad del autor.
        nacimiento : str 
            Año/fecha de nacimiento.
        muerte : str
            Año/fecha de fallecimiento.
        """
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.nacimiento = nacimiento
        self.muerte = muerte

    def show(self) -> None:
        """
         Imprime los atributos una instancia de la clase Autor.
        """
        print(f"Nombre: {self.nombre}\nNacionalidad: {self.nacionalidad}\nFecha de Nacimiento: {self.nacimiento}\nFecha de Muerte: {self.muerte}")
        
