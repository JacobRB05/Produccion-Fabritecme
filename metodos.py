import clases

procesoActual = 0

from clases import ProcesoCorte
from clases import Pieza
from clases import MaquinaCorte



mapaProcesos = {}






def agregarNuevoProceso(nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int,longitudCorte:int, maquina: MaquinaCorte, pieza:Pieza):
    proceso = ProcesoCorte(nombreProceso, DiametroInicialPieza, DiametroFinalPieza,longitudCorte, maquina, pieza)
    mapaProcesos[nombreProceso] = proceso


def agregarPieza(nombrePieza:str,material:str ):
    pieza = Pieza(nombrePieza, material)
    return pieza



diametroInicial = 50
diametroFinal = 30
longitudCorte = 100

maquina = MaquinaCorte("Torno CNC")
maquina.agregarMaterial("Acero", 150, 0.2, 500)
maquina.agregarMaterial("Aluminio", 300, 0.3, 200)

pieza = agregarPieza("Eje", "Acero")
agregarNuevoProceso("Corte Eje", diametroInicial, diametroFinal,longitudCorte,maquina, pieza)

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