import js
import metodos

# Estado interno
piezaGuardada = False
maquinaGuardada = False
materialGuardado = False

# Almacén de datos
datos = {}


def escribir_resultado(texto: str):
    """Escribe en el div #resultado sin depender de pyscript.write."""
    js.document.getElementById("resultado").innerText = texto


# ==============================
#       GUARDAR DATOS
# ==============================
def guardar_pieza(event):
    global piezaGuardada
    datos["diametro_inicial"] = float(js.document.getElementById("diametroInicial").value)
    datos["diametro_final"] = float(js.document.getElementById("diametroFinal").value)
    datos["longitud_corte"] = float(js.document.getElementById("longitudCorte").value)

    piezaGuardada = True
    escribir_resultado("✔ Parámetros de PIEZA guardados.")


def guardar_maquina(event):
    global maquinaGuardada
    datos["nombre_maquina"] = js.document.getElementById("nombreMaquina").value

    maquinaGuardada = True
    escribir_resultado("✔ Parámetros de MÁQUINA guardados.")


def guardar_material(event):
    global materialGuardado
    datos["material"] = js.document.getElementById("nombreMaterial").value
    datos["velocidad"] = float(js.document.getElementById("velocidadCorteMaterial").value)
    datos["avance"] = float(js.document.getElementById("avanceMaterial").value)
    datos["fuerza"] = float(js.document.getElementById("fuerzaCorteMaterial").value)

    materialGuardado = True
    escribir_resultado("✔ Parámetros de MATERIAL guardados.")


# ==============================
#       EJECUTAR CÁLCULO
# ==============================
def ejecutar(event):

    # Validaciones básicas
    if not piezaGuardada:
        escribir_resultado("❌ Falta guardar la PIEZA.")
        return

    if not maquinaGuardada:
        escribir_resultado("❌ Falta guardar la MÁQUINA.")
        return

    if not materialGuardado:
        escribir_resultado("❌ Falta guardar el MATERIAL.")
        return

    # LLAMADA CORRECTA A metodos.main()
    resultado = metodos.main(
        "Pieza",                      # Nombre de la pieza
        datos["material"],            # Material de la pieza
        datos["diametro_inicial"],    # Diámetro inicial
        datos["diametro_final"],      # Diámetro final
        datos["longitud_corte"],      # Longitud de corte
        datos["nombre_maquina"],      # Máquina
        datos["velocidad"],           # Velocidad corte
        datos["avance"],              # Avance por rev
        datos["fuerza"]               # Fuerza de corte
    )

    escribir_resultado(resultado)


# ==============================
#       ENLAZAR BOTONES
# ==============================
js.document.getElementById("btnGuardarPieza").addEventListener("click", guardar_pieza)
js.document.getElementById("btnGuardarMaquina").addEventListener("click", guardar_maquina)
js.document.getElementById("btnGuardarMaterial").addEventListener("click", guardar_material)
js.document.getElementById("btnEjecutar").addEventListener("click", ejecutar)
