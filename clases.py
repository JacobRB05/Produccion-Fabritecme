


class ProcesoCorte:
    nombreProceso:str
    
    DiametroInicialPieza:int
    DiametroFinalPieza:int
    ProfundidadPasada:int
    VolumenVirutaRemovido:int
    
    def __init__(self, nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int, ProfundidadPasada:int, VolumenVirutaRemovido:int):
        self.nombreProceso = nombreProceso
        self.DiametroInicialPieza = DiametroInicialPieza
        self.DiametroFinalPieza = DiametroFinalPieza
        self.ProfundidadPasada = ProfundidadPasada
        self.VolumenVirutaRemovido = VolumenVirutaRemovido
        
    
    
class Pieza:
    nombrePieza:str
    material: str

    def __init__(self, nombrePieza:str):
        self.nombrePieza = nombrePieza

    
    
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
    
   