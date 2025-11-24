from pyscript import Element
import metodos

# =============== VARIABLES GLOBALES =================
# Pieza
nombrePieza = ""
materialPieza = ""
diametroInicial = 0.0
diametroFinal = 0.0
longitudCorte = 0.0

# Máquina
nombreMaquina = ""

# Material
nombreMaterial = ""
velocidadCorteMaterial = 0
avanvePorRevolucionMaterial = 0.0
fuerzaCorteMaterial = 0

# Estados
piezaGuardada = False
maquinaGuardada = False
materialGuardado = False


# =================== GUARDAR PIEZA ===================
def guardapieza(event):
    global nombrePieza, diametroInicial, diametroFinal, longitudCorte, piezaGuardada

    try:
        diametroInicial = float(Element("diametroInicial").value)
        diametroFinal = float(Element("diametroFinal").value)
        longitudCorte = float(Element("longitudCorte").value)
        nombrePieza = "Pieza"     # Si deseas pedir nombre puedes agregar campo luego

        piezaGuardada = True
        Element("resultado").element.innerText = "✔ Datos de PIEZA guardados"
    except:
        Element("resultado").element.innerText = "❌ Error: datos inválidos en pieza"


# =================== GUARDAR MÁQUINA ===================
def guardarMaquina(event):
    global nombreMaquina, maquinaGuardada

    try:
        nombreMaquina = Element("nombreMaquina").value
        maquinaGuardada = True
        Element("resultado").element.innerText = "✔ Datos de MÁQUINA guardados"
    except:
        Element("resultado").element.innerText = "❌ Error: datos inválidos en máquina"


# =================== GUARDAR MATERIAL ===================
def guardarmaterial(event):
    global nombreMaterial, materialPieza, velocidadCorteMaterial, avanvePorRevolucionMaterial, fuerzaCorteMaterial, materialGuardado

    try:
        nombreMaterial = Element("nombreMaterial").value
        materialPieza = nombreMaterial  # La pieza usará este material

        velocidadCorteMaterial = int(Element("velocidadCorteMaterial").value)
        avanvePorRevolucionMaterial = float(Element("avanceMaterial").value)
        fuerzaCorteMaterial = int(Element("fuerzaCorteMaterial").value)

        materialGuardado = True
        Element("resultado").element.innerText = "✔ Datos de MATERIAL guardados"
    except:
        Element("resultado").element.innerText = "❌ Error: datos inválidos en material"


# =================== EJECUTAR PROCESO ===================
def ejecutar(event):
    global piezaGuardada, maquinaGuardada, materialGuardado

    if not piezaGuardada:
        Element("resultado").element.innerText = "⚠️ Falta guardar PIEZA"
        return

    if not maquinaGuardada:
        Element("resultado").element.innerText = "⚠️ Falta guardar MÁQUINA"
        return

    if not materialGuardado:
        Element("resultado").element.innerText = "⚠️ Falta guardar MATERIAL"
        return

    # Ejecutamos tu método principal
    resultado = metodos.main(
        nombrePieza,
        materialPieza,
        diametroInicial,
        diametroFinal,
        longitudCorte,
        nombreMaquina,
        velocidadCorteMaterial,
        avanvePorRevolucionMaterial,
        fuerzaCorteMaterial
    )

    Element("resultado").element.innerText = resultado

