

from pyscript import document


def guardar(event):
    nombrepieza = "Pieza"

    #Esto es toda la estructura que atiende 
    #a una de las cajitas
    input_di = document.querySelector("#diametroInicial")
    diametroInicial = input_di.value

    #El resto de cajitas
    input_df = document.querySelector("#diametroFinal")
    diametroFinal = input_df.value
    input_l = document.querySelector("#longitudCorte")
    longitudCorte = input_l.value
    input_nM = document.querySelector("#nombreMaterial")
    nombreMaterial = input_nM.value
    output_div = document.querySelector("#output")

    #input cajitas que faltaban
    input_vel = document.querySelector("#velocidadCorteMaterial")
    velocidadCorte = input_vel.value
    input_av = document.querySelector("#avanceMaterial")
    avanceMaterial = input_av.value
    input_fu = document.querySelector("#fuerzaCorteMaterial")
    fuerzaCorte = input_fu.value
    input_nom = document.querySelector("#nombreMaquina")
    nombreMaquina = input_nom.value
    

    #Falta tener la conversión a Int o float de lo necesario

    #Esto es una prueba de que sí se están tomando los parámetros
    #Respuestas del usuario
    #res = diametroInicial + diametroFinal + longitudCorte + nombreMaterial +velocidadCorte+avanceMaterial+fuerzaCorte+nombreMaquina+"\n"

    res = "\n"
    #Esto es una prueba de que si funciona python, 
    #cuando tengas todo usa main(p1,p2,...) en vez de
    #main2(), si acaso mira que hace
    #TE AMOOOOO
    
    res+= main2(diametroInicial, diametroFinal, longitudCorte, nombreMaterial, velocidadCorte, avanceMaterial, fuerzaCorte, nombreMaquina)
    output_div.innerText = (res)

class Pieza:
    nombrePieza:str
    material: str

    def __init__(self, nombrePieza:str, material:str):
        self.nombrePieza = nombrePieza
        self.material = material
    
class MaquinaCorte:
    
    nombreMaquina:str
    velocidadCorte: dict [str, int]
    avancePorRevolucion: dict [str, float]
    fuerzaCorte: dict [str, int]
   
    def __init__(self, nombreMaquina:str):
        self.nombreMaquina = nombreMaquina
        self.velocidadCorte: dict[str, int] = {}
        self.avancePorRevolucion: dict[str, float] = {}
        self.fuerzaCorte: dict[str, int] = {}
            
    def agregarMaterial(self, material:str, velocidadCorte:int, avancePorRevolucion:float,fuerzaCorte:int):
        self.velocidadCorte[material] = velocidadCorte
        self.avancePorRevolucion[material] = avancePorRevolucion
        self.fuerzaCorte[material] = fuerzaCorte

    def getVelocidadMaterial(self,material:str):
        return self.velocidadCorte[material]

    def getAvancePorRevolucion(self,material:str):
        return self.avancePorRevolucion[material]

    def getFuerzaCorte(self,material:str):
        return self.fuerzaCorte[material]
    
class ProcesoCorte:
    nombreProceso:str
    
    diametroInicialPieza:float
    diametroFinalPieza:float
    longitudCorte:float
    pieza:Pieza
    maquina:MaquinaCorte
    
    profundidadPasada:int
    volumenVirutaRemovido:int

    velocdadRotacion:float
    

    def __init__(self, nombreProceso:str, DiametroInicialPieza:float, DiametroFinalPieza:float,longitudCorte:float, maquina:MaquinaCorte,pieza:Pieza):
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
def agregarNuevoProceso(nombreProceso:str, DiametroInicialPieza:float, DiametroFinalPieza:float,longitudCorte:float, nombreMaquina: str, nombrePieza:str):
    pieza = mapaPiezas.get(nombrePieza)
    maquina = mapaMaquinas.get(nombreMaquina)
    proceso = ProcesoCorte(nombreProceso, DiametroInicialPieza, DiametroFinalPieza,longitudCorte, maquina, pieza)
    mapaProcesos[nombreProceso] = proceso


def agregarPieza(nombrePieza:str,material:str ):
    pieza = Pieza(nombrePieza, material)
    mapaPiezas[nombrePieza] = pieza
    return pieza

def agregarMaquinaCorte(nombreMaquina:str):
    maquina = MaquinaCorte(nombreMaquina)
    mapaMaquinas[nombreMaquina] = maquina
    return maquina

def agregarMaterialMaquina(nombreMaquina:str, material:str, velocidadCorte:int, avancePorRevolucion:float,fuerzaCorte:int):
    maquina = mapaMaquinas.get(nombreMaquina)
    if maquina:
        maquina.agregarMaterial(material, velocidadCorte, avancePorRevolucion,fuerzaCorte)
    else:
        print(f"La maquina {nombreMaquina} no existe en el mapa de maquinas.")




def getmsg():
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    msg = ""
    
    velocidadRotacion = mapaProcesos["Proceso"].getVelocidadRotacion()
    msg+= f"La velocidad de rotacion es: {round(velocidadRotacion,3)} RPM" + "\n"
    
    avancePorMinuto = mapaProcesos["Proceso"].getAvancePorMinuto()
    msg+= f"El avance por minuto es: {round(avancePorMinuto,3)} mm/min"+ "\n"

    profundidadPasada = mapaProcesos["Proceso"].profundidadPasada
    msg+= f"La profundidad de pasada es: {round(profundidadPasada,3)} mm"+ "\n"

    tiempoProceso = mapaProcesos["Proceso"].getTiempoProceso()
    msg+= f"El tiempo del proceso es: {round(tiempoProceso,3)} minutos"+  "\n"

    volumenViruta = mapaProcesos["Proceso"].getVolumenVirutaRemovido()
    msg+= f"El volumen de viruta removido es: {round(volumenViruta,3)} cm³" + "\n"

    potenciaCorte = mapaProcesos["Proceso"].getPotenciaCorte()
    msg+= f"La potencia de corte es: {round(potenciaCorte,3)} kW"+ "\n"
    
    
    return msg




# Crear maquina, agregar materiales, crear pieza y proceso
def main(nombrePieza:str, materialPieza:str, diametroInicial:float, diametroFinal:float, longitudCorte:float, nombreMaquina:str, velocidadCorteMaterial:int, avancePorRevolucionMaterial:float, fuerzaCorteMaterial:int):
    agregarMaquinaCorte(nombreMaquina)
    agregarMaterialMaquina(nombreMaquina, materialPieza, velocidadCorteMaterial, avancePorRevolucionMaterial, fuerzaCorteMaterial)
    agregarPieza(nombrePieza, materialPieza)
    agregarNuevoProceso("Proceso", diametroInicial, diametroFinal,longitudCorte,nombreMaquina, nombrePieza)
    return getmsg()

def main2(diametroInicial, diametroFinal, longitudCorte, materialPieza, velocidadCorteMaterial, avancePorRevolucionMaterial, fuerzaCorteMaterial, nombreMaquina):
    nombrePieza = "Pieza"
    
    #inputs
        #Parametros Pieza
    diametroInicial = float(diametroInicial)
    diametroFinal = float(diametroFinal)
    longitudCorte = float(longitudCorte)
    #materialPieza = "Acero"
        #Parametros Maquina
    #nombreMaquina = "Torno CNC"
        #Parametros Material
    velocidadCorteMaterial = int(velocidadCorteMaterial)
    avancePorRevolucionMaterial = float(avancePorRevolucionMaterial)
    fuerzaCorteMaterial = int(fuerzaCorteMaterial)
    
    msg = main(nombrePieza, materialPieza, diametroInicial, diametroFinal, longitudCorte, nombreMaquina, velocidadCorteMaterial, avancePorRevolucionMaterial, fuerzaCorteMaterial)
    return msg