
class Pieza:
    nombrePieza:str
    material: str

    def __init__(self, nombrePieza:str, material:str):
        self.nombrePieza = nombrePieza
        self.material = material
    
class MaquinaCorte:
    
    nombreMaquina:str
    velocidadCorte: dict [str, int]
    avancePorRevolucion: dict [str, int]
    fuerzaCorte: dict [str, int]
   
    def __init__(self, nombreMaquina:str):
        self.nombreMaquina = nombreMaquina
        self.velocidadCorte: dict[str, int] = {}
        self.avancePorRevolucion: dict[str, int] = {}
        self.fuerzaCorte: dict[str, int] = {}
            
    def agregarMaterial(self, material:str, velocidadCorte:int, avancePorRevolucion:int,fuerazaCorte:int):
        self.velocidadCorte[material] = velocidadCorte
        self.avancePorRevolucion[material] = avancePorRevolucion
        self.fuerzaCorte[material] = fuerazaCorte

    def getVelocidadMaterial(self,material:str):
        return self.velocidadCorte[material]

    def getAvancePorRevolucion(self,material:str):
        return self.avancePorRevolucion[material]

    def getFuerzaCorte(self,material:str):
        return self.fuerzaCorte[material]
    
class ProcesoCorte:
    nombreProceso:str
    
    diametroInicialPieza:int
    diametroFinalPieza:int
    longitudCorte:int
    pieza:Pieza
    maquina:MaquinaCorte
    
    profundidadPasada:int
    volumenVirutaRemovido:int

    velocdadRotacion:int
    

    def __init__(self, nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int,longitudCorte:int, maquina:MaquinaCorte,pieza:Pieza):
        self.nombreProceso = nombreProceso
        self.diametroInicialPieza = DiametroInicialPieza
        self.diametroFinalPieza = DiametroFinalPieza
        self.pieza = pieza
        self.profundidadPasada = (DiametroInicialPieza - DiametroFinalPieza) / 2
        self.volumenVirutaRemovido = 0
        self.longitudCorte = longitudCorte
        self.maquina = maquina
        self.velocdadRotacion = self.getVelocidadRotacion()


    def getVelocidadRotacion (self):
        velocidadCorte = self.maquina.getVelocidadMaterial(self.pieza.material)
        return (velocidadCorte * 1000) / (3.14 * self.diametroInicialPieza)
    
    def getLongitudCorte (self):
        return self.longitudCorte
    def getAvancePorMinuto (self):
        return self.maquina.getAvancePorRevolucion(self.pieza.material) * self.getVelocidadRotacion()
    def getTiempoProceso (self):
        avancePorMinuto = self.getAvancePorMinuto()
        return self.longitudCorte / self.getAvancePorMinuto()
    def getVolumenVirutaRemovido (self):
        volumen = self.profundidadPasada *self.maquina.getAvancePorRevolucion(self.pieza.material) * self.maquina.getVelocidadMaterial(self.pieza.material)
        return volumen
    def getPotenciaCorte (self):
        fuerzaCorte = self.maquina.getFuerzaCorte(self.pieza.material)
        velocidadCorte = self.maquina.getVelocidadMaterial(self.pieza.material)
        potencia = (fuerzaCorte * velocidadCorte) / 60000
        return potencia