
import arrr
from pyscript import document


def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = arrr.translate(english) + "I love you mateeee"
    
def translate_español(event):
    input_text = document.querySelector("#español")
    english = input_text.value
    output_div = document.querySelector("#output2")
    res = arrr.translate(english) + "Te amo mateeee"
    output_div.innerText = res