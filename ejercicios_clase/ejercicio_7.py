#Ejercicio con listas
def cuadrados(lista_numeros):
    lista_cuadraddos=[]
    for elemento in lista_numeros:
        cuadrado = elemento ** 2
        lista_cuadraddos.append(cuadrado)
    return print(lista_cuadraddos)

lista=[1,2,3,4,5,6]
cuadrados(lista)
