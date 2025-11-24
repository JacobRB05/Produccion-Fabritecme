from metodos import main as metodo_main
from pyscript import document
nombre_pieza: str 
nombre_pieza = "Pieza"
diametro_inicial: float
diametro_final: float
longitud_corte: float

def guardarPieza(event):
    diametro_inicial = float(document.querySelector("#diametroInicial").value)
    diametro_final = float(document.querySelector("#diametroFinal").value)
    longitud_corte = float(document.querySelector("#longitudCorte").value)


nombre_material: str
velocidad_corte_material: int
avance_por_revolucion_material: float
fuerza_corte_material: int

def guardarMaterial(event):
    nombre_material = document.querySelector("#nombreMaterial").value
    velocidad_corte_material = int(document.querySelector("#velocidadCorteMaterial").value)
    avance_por_revolucion_material = float(document.querySelector("#avancePorRevolucionMaterial").value)
    fuerza_corte_material = int(document.querySelector("#fuerzaCorteMaterial").value)
    
    
nombre_maquina: str
def guardarMaquina(event):
    nombre_maquina = document.querySelector("#nombreMaquina").value
    
def main(event):

    resultado = metodo_main(
        nombre_pieza,
        nombre_material,
        diametro_inicial,
        diametro_final,
        longitud_corte,
        nombre_maquina,
        velocidad_corte_material,
        avance_por_revolucion_material,
        fuerza_corte_material
    )

    output_div = document.querySelector("#resultado")
    output_div.innerText = resultado