import clases
from clases import ProcesoCorte
from clases import Pieza
from clases import MaquinaCorte


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



