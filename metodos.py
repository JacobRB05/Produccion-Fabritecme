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


#inputs

diametroInicial = 50
diametroFinal = 30
longitudCorte = 100
nombreMaquina = "Torno CNC"


# Crear maquina, agregar materiales, crear pieza y proceso

agregarMaquinaCorte(nombreMaquina)
agregarMaterialMaquina(nombreMaquina, "Acero", 150, 0.2, 500)
agregarMaterialMaquina(nombreMaquina,"Aluminio", 300, 0.3, 200)
agregarPieza("Eje", "Acero")
agregarNuevoProceso("Corte Eje", diametroInicial, diametroFinal,longitudCorte,nombreMaquina, "Eje")


#outputs


velocidadRotacion = mapaProcesos["Corte Eje"].getVelocidadRotacion()
print(f"La velocidad de rotacion es: {velocidadRotacion} RPM")

avancePorMinuto = mapaProcesos["Corte Eje"].getAvancePorMinuto()
print(f"El avance por minuto es: {avancePorMinuto} mm/min")

profundidadPasada = mapaProcesos["Corte Eje"].profundidadPasada
print(f"La profundidad de pasada es: {profundidadPasada} mm")

tiempoProceso = mapaProcesos["Corte Eje"].getTiempoProceso()
print(f"El tiempo del proceso es: {tiempoProceso} minutos")

volumenViruta = mapaProcesos["Corte Eje"].getVolumenVirutaRemovido()
print(f"El volumen de viruta removido es: {volumenViruta} mm³")

potenciaCorte = mapaProcesos["Corte Eje"].getPotenciaCorte()
print(f"La potencia de corte es: {potenciaCorte} kW")   
print("hola mundo")