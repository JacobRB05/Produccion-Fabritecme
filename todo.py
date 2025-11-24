
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
    
    # Mapas para almacenar las instancias de piezas, maquinas y procesos
mapaProcesos = {}
mapaMaquinas = {}
mapaPiezas = {}




# Funciones para manejar los procesos de corte
def agregarNuevoProceso(nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int,longitudCorte:int, nombreMaquina: str, nombrePieza:str):
    pieza = mapaPiezas.get(nombrePieza)
    proceso = ProcesoCorte(nombreProceso, DiametroInicialPieza, DiametroFinalPieza,longitudCorte, mapaMaquinas.get(nombreMaquina), pieza)
    mapaProcesos[nombreProceso] = proceso


def agregarPieza(nombrePieza:str,material:str ):
    pieza = Pieza(nombrePieza, material)
    mapaPiezas[nombrePieza] = pieza
    return pieza

def agregarMaquinaCorte(nombreMaquina:str):
    maquina = MaquinaCorte(nombreMaquina)
    mapaMaquinas[nombreMaquina] = maquina
    return maquina

def agregarMaterialMaquina(nombreMaquina:str, material:str, velocidadCorte:int, avancePorRevolucion:int,fuerzaCorte:int):
    maquina = mapaMaquinas.get(nombreMaquina)
    if maquina:
        maquina.agregarMaterial(material, velocidadCorte, avancePorRevolucion,fuerzaCorte)
    else:
        print(f"La maquina {nombreMaquina} no existe en el mapa de maquinas.")




def getmsg():
    msg = ""
    velocidadRotacion = mapaProcesos["Proceso"].getVelocidadRotacion()
    msg+= f"La velocidad de rotacion es: {velocidadRotacion} RPM" + "\n"

    avancePorMinuto = mapaProcesos["Proceso"].getAvancePorMinuto()
    msg+= f"El avance por minuto es: {avancePorMinuto} mm/min"+ "\n"

    profundidadPasada = mapaProcesos["Proceso"].profundidadPasada
    msg+= f"La profundidad de pasada es: {profundidadPasada} mm"+ "\n"

    tiempoProceso = mapaProcesos["Proceso"].getTiempoProceso()
    msg+= f"El tiempo del proceso es: {tiempoProceso} minutos"+  "\n"

    volumenViruta = mapaProcesos["Proceso"].getVolumenVirutaRemovido()
    msg+= f"El volumen de viruta removido es: {volumenViruta} cm³" + "\n"

    potenciaCorte = mapaProcesos["Proceso"].getPotenciaCorte()
    msg+= f"La potencia de corte es: {potenciaCorte} kW"+ "\n"
    return msg




# Crear maquina, agregar materiales, crear pieza y proceso
def main(nombrePieza:str, materialPieza:str, diametroInicial:float, diametroFinal:float, longitudCorte:float, nombreMaquina:str, velocidadCorteMaterial:int, avanvePorRevolucionMaterial:float, fuerzaCorteMaterial:int):
    agregarMaquinaCorte(nombreMaquina)
    agregarMaterialMaquina(nombreMaquina, materialPieza, velocidadCorteMaterial, avanvePorRevolucionMaterial, fuerzaCorteMaterial)
    agregarPieza(nombrePieza, materialPieza)
    agregarNuevoProceso("Proceso", diametroInicial, diametroFinal,longitudCorte,nombreMaquina, nombrePieza)
    return getmsg()

if __name__ == "__main__":
    #inputs
        #Parametros Pieza
    diametroInicial = 50
    diametroFinal = 30
    longitudCorte = 100 
    nombrePieza = "Pieza"
    materialPieza = "Acero"
        #Parametros Maquina
    nombreMaquina = "Torno CNC"
        #Parametros Material
    velocidadCorteMaterial = 150
    avanvePorRevolucionMaterial = 0.2
    fuerzaCorteMaterial = 500
    msg = main(nombrePieza, materialPieza, diametroInicial, diametroFinal, longitudCorte, nombreMaquina, velocidadCorteMaterial, avanvePorRevolucionMaterial, fuerzaCorteMaterial)
    print(msg)


