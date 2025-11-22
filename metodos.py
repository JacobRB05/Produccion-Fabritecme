import clases

procesoActual = 0

from clases import ProcesoCorte
from clases import Pieza
from clases import MaquinaCorte


mapaProcesos = {}


def agregarPieza(nombrePieza:str,material:str ):
    pieza = Pieza(nombrePieza, material)
    return pieza

def agregarNuevoProceso(nombreProceso:str, DiametroInicialPieza:int, DiametroFinalPieza:int,pieza:Pieza):
    proceso = ProcesoCorte(nombreProceso, DiametroInicialPieza, DiametroFinalPieza, pieza)
    mapaProcesos[nombreProceso] = proceso


maquina = MaquinaCorte("Torno CNC")
maquina.agregarMaterial("Acero", 150, 0.2)
maquina.agregarMaterial("Aluminio", 300, 0.3)


diametroInicial = 50
diametroFinal = 30

pieza = agregarPieza("Eje", "Acero")
agregarNuevoProceso("Corte Eje", diametroInicial, diametroFinal, pieza)

print("hola mundo")