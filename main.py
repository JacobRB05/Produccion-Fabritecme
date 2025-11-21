
import arrr
from pyscript import document


def funcion1(event):
    input_text = document.querySelector("#button1")
    value1 = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerHTML = f"El valor ingresado es: {int(value1)**2}"
    
