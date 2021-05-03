# Crear una funcion que tome una cadena y la reescriba en orden inverso.
'''
def revertir_cadena(cadena):
    cadena_invertida=cadena[::-1]
    return print(f"La cadena invertida es: {cadena_invertida}")

revertir_cadena('Escalera')
'''
cadena='Escalera'
cadena_invertida=(lambda cadena : cadena[::-1])
print(f"La cadena invertida es: {cadena_invertida(cadena)}")