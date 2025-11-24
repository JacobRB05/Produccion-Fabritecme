import js
import pyscript
import metodos

# Variables globales (estado guardado)
piezaGuardada = False
maquinaGuardada = False
materialGuardado = False

# Datos almacenados
datos = {}

def guardar_pieza(event):
    global piezaGuardada
    datos["diametro_inicial"] = float(js.document.getElementById("diametroInicial").value)
    datos["diametro_final"] = float(js.document.getElementById("diametroFinal").value)
    datos["longitud_corte"] = float(js.document.getElementById("longitudCorte").value)

    piezaGuardada = True
    pyscript.write("resultado", "✔ Parámetros de PIEZA guardados.")


def guardar_maquina(event):
    global maquinaGuardada
    datos["nombre_maquina"] = js.document.getElementById("nombreMaquina").value

    maquinaGuardada = True
    pyscript.write("resultado", "✔ Parámetros de MÁQUINA guardados.")


def guardar_material(event):
    global materialGuardado
    datos["nombre_material"] = js.document.getElementById("nombreMaterial").value
    datos["velocidad"] = float(js.document.getElementById("velocidadCorteMaterial").value)
    datos["avance"] = float(js.document.getElementById("avanceMaterial").value)
    datos["fuerza"] = float(js.document.getElementById("fuerzaCorteMaterial").value)

    materialGuardado = True
    pyscript.write("resultado", "✔ Parámetros de MATERIAL guardados.")


def ejecutar(event):
    if not (piezaGuardada and maquinaGuardada and materialGuardado):
        pyscript.write("resultado", "❌ Primero guarde pieza, máquina y material.")
        return

    # Llamada a tu método principal
resultado = metodos.main(
    "Pieza",                     # nombre de la pieza (puedes poner otro)
    datos["nombre_material"],    # material de la pieza
    datos["diametro_inicial"],
    datos["diametro_final"],
    datos["longitud_corte"],
    datos["nombre_maquina"],
    datos["velocidad"],
    datos["avance"],
    datos["fuerza"]
    )


pyscript.write("resultado", resultado)


# ======== ENLAZAR EVENTOS ========
js.document.getElementById("btnGuardarPieza").addEventListener("click", guardar_pieza)
js.document.getElementById("btnGuardarMaquina").addEventListener("click", guardar_maquina)
js.document.getElementById("btnGuardarMaterial").addEventListener("click", guardar_material)
js.document.getElementById("btnEjecutar").addEventListener("click", ejecutar)
