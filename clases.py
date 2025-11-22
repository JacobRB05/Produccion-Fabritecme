
class Pieza:
    nombrePieza:str
    material: str

    def __init__(self, nombrePieza:str, material:str):
        self.nombrePieza = nombrePieza
        self.material = material


class ProcesoCorte:
    nombreProceso:str
    
    DiametroInicialPieza:int
    DiametroFinalPieza:int
    ProfundidadPasada:int
    VolumenVirutaRemovido:int
    pieza:Pieza

    def __init__(self, nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int, pieza:Pieza):
        self.nombreProceso = nombreProceso
        self.DiametroInicialPieza = DiametroInicialPieza
        self.DiametroFinalPieza = DiametroFinalPieza
        self.pieza = pieza
        self.ProfundidadPasada = (DiametroInicialPieza - DiametroFinalPieza) / 2
        


    
    def __init__(self, nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int, pieza:Pieza):
        self.nombreProceso = nombreProceso
        self.DiametroInicialPieza = DiametroInicialPieza
        self.DiametroFinalPieza = DiametroFinalPieza
        self.ProfundidadPasada = (DiametroInicialPieza - DiametroFinalPieza) / 2

        
    
    

    
    
class MaquinaCorte:
    
    nombreMaquina:str
   
    velocidadCorte: dict [str, int]
    avancePorRevolucion: dict [str, int]
   
    def __init__(self, nombreMaquina:str):
        self.nombreMaquina = nombreMaquina
        self.velocidadCorte: dict[str, int] = {}
        self.avancePorRevolucion: dict[str, int] = {}
            
    def agregarMaterial(self, material:str, velocidadCorte:int, avancePorRevolucion:int):
        self.velocidadCorte[material] = velocidadCorte
        self.avancePorRevolucion[material] = avancePorRevolucion

    def getVelocidadMaterial(self,material:str):
        return self.velocidadCorte[material]

    def getAvancePorRevolucion(self,material:str):
        return self.avancePorRevolucion[material]

