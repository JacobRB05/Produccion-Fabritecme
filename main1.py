
import arrr
from pyscript import document


def funcion1(event):
    input_nombrePieza = document.querySelector("#nombrePieza")
    nombrePieza = input_nombrePieza.value
    output_div = document.querySelector("#output")  
    output_div.innerHTML = f"El valor ingresado es: {nombrePieza}"
    
