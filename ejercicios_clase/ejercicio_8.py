# Definir una función que recibe una candtidad indeterminada de números
# y los suma.

def funcion_sumatorio(*numeros):
    sumatorio=0
    for numero in numeros:
        sumatorio= sumatorio + numero
    return print(f"El sumatorio de los numeros es: {sumatorio}")

funcion_sumatorio(1,2,3,4,5,10,20)
        