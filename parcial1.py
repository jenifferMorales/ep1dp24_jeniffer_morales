#clase padre
class Ciudad:
    def __init__(self, nom,cod):
        self.nombre= nom
        self.codigo=cod
    
    def mostrar(self):
        print(f"El nombre de la ciudad es: {self.nombre} y el codigo es: {self.codigo}")

ejemplo=Ciudad("Ciudad 1", 10)


#clase hija
class Estado(Ciudad):
    def __init__(self, nom, cod, codE, nomE, desc):
        super().__init__(nom,cod)
        self.codigoE=codE
        self.nombreE=nomE
        self.descripcion=desc
    
    def mostrarEstado(self):
        print(f"El nombre del estado es: {self.nombreE} el codigo del estado es: {self.codigoE}")
    
estado=Estado("ciudad 1", 10, 110, "estado 1", "descripcion 1")


class Pais(Estado):
    def __init__(self, nom, cod, codE, nomE, desc, nomP, codP):
        super().__init__(nom, cod, codE, nomE, desc)
        self.nombreP=nomP
        self.codigoP = codP
    
    def mostrarPais(self):
        print(f"el nombre del pais es: {self.nombreP}")

pais=Pais("ciudad 1", 10, 110, "estado 1", "descripcion 1", "pais 1", 90)


class Continente(Pais):
    def __init__(self, nom, cod, codE, nomE, desc, nomP, codP, nomC, codC):
        super().__init__(nom, cod, codE, nomE, desc, nomP, codP)
        self.nombreC=nomC
        self.codigoC=codC
    def mostrarContinente(self):
        print(f"El codigo el continente es: {self.codigoC}")

continente= Continente("ciudad 1", 10, 110, "estado 1", "descripcion 1", "pais 1", 90, "continente 1", 340)
continente.mostrar()
continente.mostrarEstado()
continente.mostrarPais()
continente.mostrarContinente()
