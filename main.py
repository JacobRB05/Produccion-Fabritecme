from metodos import main as metodo_main
from js import document
nombre_pieza: str 
nombre_pieza = "Pieza"
diametro_inicial: float
diametro_final: float
longitud_corte: float

def guardarPieza(event):
    global nombre_pieza, diametro_inicial, diametro_final, longitud_corte
    diametro_inicial = float(document.querySelector("#diametroInicial").value)
    diametro_final = float(document.querySelector("#diametroFinal").value)
    longitud_corte = float(document.querySelector("#longitudCorte").value)


nombre_material: str
velocidad_corte_material: int
avanceMaterial: float
fuerza_corte_material: int

def guardarMaterial(event):
    global nombre_material, velocidad_corte_material, avanceMaterial, fuerza_corte_material
    nombre_material = document.querySelector("#nombreMaterial").value
    velocidad_corte_material = int(document.querySelector("#velocidadCorteMaterial").value)
    avanceMaterial = float(document.querySelector("#avanceMaterial").value)
    fuerza_corte_material = int(document.querySelector("#fuerzaCorteMaterial").value)
    
    
nombre_maquina: str

def guardarMaquina(event):
    global nombre_maquina
    nombre_maquina = document.querySelector("#nombreMaquina").value
    
def main():

    resultado = metodo_main(
        nombre_pieza,
        nombre_material,
        diametro_inicial,
        diametro_final,
        longitud_corte,
        nombre_maquina,
        velocidad_corte_material,
        avanceMaterial,
        fuerza_corte_material
    )

    output_div = document.querySelector("#resultado")
    output_div.innerText = resultado