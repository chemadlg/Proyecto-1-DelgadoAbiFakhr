class Obra:
    """
    Representa una obra de arte del Museo.

    Atributos
    id : int
        Identificador único de la obra.
    titulo : str
        Título o nombre de la obra.
    departamento : Departamento
        Instancia de Departamento al que pertenece la obra.
    autor : Autor
        Instancia de Autor que creó la obra.
    tipo : str
        Clasificación o tipo de la obra
    anio : str
        Año en que fue creada la obra.
    imagen : str
        URL de la imagen representativa de la obra.
    """
    def __init__(self, id, titulo, departamento, autor, tipo, anio, imagen):
        """
        Inicializa una nueva instancia de Obra.

        Parámetros
        id : int
            Identificador único de la obra.
        titulo : str
            Título o nombre de la obra.
        departamento : Departamento
            Departamento al que pertenece la obra.
        autor : Autor
            Autor que creó la obra.
        tipo : str
            Clasificación o tipo de la obra.
        anio : str | int
            Año de creación.
        imagen : str
            URL de la imagen de la obra.
        """
        self.id = id
        self.titulo = titulo
        self.departamento = departamento
        self.autor = autor
        self.tipo = tipo
        self.anio = anio
        self.imagen = imagen

    def mostrar(self):
        """
        Imprime los atributos una instancia de la clase Obra.
        """
        print(f"ID: {self.id}\nTitulo: {self.titulo}\nDepartamento: {self.departamento.nombre}\nAutor:\n{self.autor.mostrar()}\nTipo: {self.tipo}\nAño de Creacion: {self.anio}\nImagen: {self.imagen}")