
class Pieza:
    nombrePieza:str
    material: str

    def __init__(self, nombrePieza:str, material:str):
        self.nombrePieza = nombrePieza
        self.material = material


class ProcesoCorte:
    nombreProceso:str
    
    diametroInicialPieza:int
    diametroFinalPieza:int
    profundidadPasada:int
    volumenVirutaRemovido:int
    longitudCorte:int
    
    pieza:Pieza

    def __init__(self, nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int, pieza:Pieza):
        self.nombreProceso = nombreProceso
        self.diametroInicialPieza = DiametroInicialPieza
        self.diametroFinalPieza = DiametroFinalPieza
        self.pieza = pieza
        self.profundidadPasada = (DiametroInicialPieza - DiametroFinalPieza) / 2
        self.volumenVirutaRemovido = 0
        self.longitudCorte = 0
        
    
    

    
    
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
            
    def agregarMaterial(self, material:str, velocidadCorte:int, avancePorRevolucion:int):
        self.velocidadCorte[material] = velocidadCorte
        self.avancePorRevolucion[material] = avancePorRevolucion

    def getVelocidadMaterial(self,material:str):
        return self.velocidadCorte[material]

    def getAvancePorRevolucion(self,material:str):
        return self.avancePorRevolucion[material]

