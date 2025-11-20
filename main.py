def calcular_doble(valor):
    """
    Función sencilla para demostrar que el código
    se ejecuta desde un archivo Python externo.
    """
    try:
        valor = int(valor)
        return valor * 2
    except:
        return "Entrada no válida"
