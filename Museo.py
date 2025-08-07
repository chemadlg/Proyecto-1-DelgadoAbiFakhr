import requests
from Departamento import Departamento
from Autor import Autor

class Museo:
    def __init__(self):
        self.deptos = []
        self.autores = []
        self.obras = []
        self.nacionalidades = []

    def cargar_datos(self):
        response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")

        data = response.json()

        # Recorremos cada departamento recibido
        for info_depto in data["departments"]:

            depto_id = info_depto["departmentId"]       
            nombre = info_depto["displayName"]

            # Creamos la instancia y la guardamos en la lista de deptos
            self.deptos.append(Departamento(depto_id, nombre))

        #Luego cargar el CSV con las nacionalidades

    def obras_depto(self):

        #Mostrar los departamentos disponibles
        print("\nDepartamentos Disponibles:")
        for depto in self.deptos:
            print(f"{depto.id} - {depto.nombre}")

        #Elegir el departamento a traves del id
        opcion = input("Ingresa el id del depto: ")
        while not opcion.isnumeric() or self.buscar_depto_id(int(opcion)) == None:
            print("Error! El id debe ser numerio y debe ser un id valido.")
            opcion = input("Ingresa el id del depto: ")

        #Buscar y obtener una instacia de la clase Departamento a traves del id
        depto_selecccionado = self.buscar_depto_id(int(opcion))
        
        #Buscar las obras correspondientes al id seleccionado por el usuario
        response = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={depto_selecccionado.id}")

        #Respuesta de la API en json
        data = response.json()

        #Total de obras obtenidas
        total_obras = len(data["objectIDs"])
        num_lote = 0 #numero de lotes el cual ira varian de 10 en 1o

        #Iterar mientra el ote sea menor al total de las obras
        while num_lote < total_obras:
            
            #Obtener un sublista el cual ira desde el num_lote de la lista de obras hasta el numero de lote mas 10
            ids_actual = data["objectIDs"][num_lote: num_lote+10]
            
            #iterar sobre la lista de ids correspondiente al bloque actual para mostrarlas al usuario
            for id_act in ids_actual:
                response_obra = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_act}")

                data_obra = response_obra.json()

                #Verifico si la obra ya la tengo registrada o no y muestro sus datos
                #Debe ser a traves del id el cual es unico ya que algunos nombres se repiten

                self.buscar_crear_obra(data_obra["objectID"])


    def buscar_crear_obra(self, id):
        pass


    def buscar_depto_id(self, id):
        if len(self.deptos) != 0:
            for depto in self.deptos:
                if depto.id == id:
                    return depto
        
        return None

    def obras_nacionalidad(self):
        pass

    def obras_autor(self):
        pass

    def iniciar(self):
        #Cargar los departamentos y el CSV
        self.cargar_datos()

        #Mostrar el menu dentro del While True
        while True:
            print("\n**************************************")
            print("       Bienvenidos a MetroArt")
            print("**************************************")

            print("1. Ver lista de obras por Departamento.\n2. Ver lista de obras por Nacionalidad del autor.\n3. Ver lista de obras por nombre del autor.\n4. Salir")

            opcion = input("\nIngrese la opcion deseada: ")
            
            if opcion == "1":
                self.obras_depto()
            elif opcion =="2":
                self.obras_nacionalidad()
            elif opcion=="3":
                self.obras_autor()
            elif opcion=="4":
                print("\nGracias por utilizar MatroArt.")
                break
            else:
                print("\nOpcion Invalida!\n")
