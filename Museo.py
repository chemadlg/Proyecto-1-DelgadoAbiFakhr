import requests
import time
from Departamento import Departamento
from Autor import Autor
from Obra import Obra

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
        with open('CH_Nationality_List_20171130_v1.csv', encoding='utf-8') as archivo:
            next(archivo)  # saltamos la primera línea (cabecera)
            for linea in archivo:
                linea = linea.strip()
                if linea:  # ignoramos líneas vacías
                    self.nacionalidades.append(linea)

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

                if response_obra.status_code == 200:
                    data_obra = response_obra.json()

                    #Verifico si la obra ya la tengo registrada o no y muestro sus datos
                    #Debe ser a traves del id el cual es unico ya que algunos nombres se repiten

                    obra = self.buscar_crear_obra(data_obra, depto_selecccionado)
                    
                    #Muestro la obra
                    print("")
                    obra.show()
                    print("")

            num_lote += 10
            if num_lote >= total_obras:
                break

            time.sleep(3)

            seguir=input("\nDeseas Mostrar 10 obras mas?\n1. Si \n2. No\n ")
            while not seguir.isnumeric() or not int(seguir) in range(1,3):
                print("Error! Ingresa 1 si quieres seguir viendo y 2 si no quieres ver mas")
                seguir=input("\nDeseas Mostrar 10 obras mas?\n1. Si \n2. No\n ")

            if seguir == "2":
                break

    def buscar_crear_obra(self, data_obra, depto_selecccionado):
        #Buscar si la obra ya esta registrada
        for obra in self.obras:
            if obra.id == data_obra["objectID"]:
                #Si encuentro una obra que coincida con el id la devuelvo
                return obra
        
        #Si nunca llego al return dentro del bucle entonces al salir del bucle creo la obra
        id = data_obra["objectID"]
        titulo=data_obra["title"]
        departamento=depto_selecccionado

        #Verifico si el autro existe y lo traigo y sin no lo creo
        autor=self.buscar_crear_autor(data_obra)
        tipo=data_obra["classification"]
        anio=data_obra["objectDate"]
        imagen=data_obra["primaryImage"]

        #Creo un objeto de la clase obra y lo añado a mi lista de obras
        obra_nueva = Obra(id, titulo, departamento, autor, tipo, anio, imagen)
        self.obras.append(obra_nueva)
        
        #Devuelvo la obra
        return obra_nueva

    
    def buscar_crear_autor(self, data):
        #Buscar si el autor ya esta registrado
        for autor in self.autores:
            if autor.nombre == data["artistDisplayName"]:
                #Retorno el autor si encuentro uno que coincida con el nombre
                return autor
        
        #Si nunca llego al return dentro del bucle entonces al salir del bucle creo al autor
        nombre=data["artistDisplayName"]
        nacionalidad=data["artistNationality"]
        nacimiento=data["artistBeginDate"]
        muerte=data["artistEndDate"]

        #Creo un objeto de la clase autor y lo añado a mi lista de autores
        autor_nuevo = Autor(nombre, nacionalidad, nacimiento, muerte)
        self.autores.append(autor_nuevo)

        #Devuelvo al autor
        return autor_nuevo

    def buscar_depto_id(self, id):
        if len(self.deptos) != 0:
            for depto in self.deptos:
                if depto.id == id:
                    return depto
        
        return None

    def obras_nacionalidad(self):
        print("\nNacionalidades Disponibles:")
        count = 1
        for nac in self.nacionalidades:
            print(f"{count}. {nac}")
            count += 1

        #Elegir el numero correspondiente a la nacionalidad
        opcion = input("Ingresa el numero correspondiente a la nacionalidad deseada: ")
        while not opcion.isnumeric() or not int(opcion) in range(1, count+1):
            print("Error! El id debe ser numerio y debe ser un id valido.")
            opcion = input("Ingresa el numero correspondiente a la nacionalidad deseada: ")

        nac_select = self.nacionalidades[int(opcion)-1]

        print(f"Haz seleccionado {nac_select}")

    def obras_autor(self):
        nombre = input("Ingrese el nombre del autor: ").lower()
        obras_encontradas = []
        for obra in self.obras:
            if obra.autor.nombre.lower() == nombre:
                obras_encontradas.append(obra)

        if len(obras_encontradas) != 0:
            for obra in obras_encontradas:
                obra.show()
        else:
            print("No se encontraron obras de ese autor")

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
