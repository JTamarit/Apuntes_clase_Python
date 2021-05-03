# Definir una función que compruebe si un número está en un intervalo
# determinado
def comprobar_valor(*argumentos):
    if valor in range(intervalo[0],intervalo[1]):
        print(f"El valor {valor} está dentro del intervalo ({intervalo[0]}-{intervalo[1]})")
    else:
        print(f"El valor {valor} no está dentro del intervalo ({intervalo[0]}-{intervalo[1]})")

valor = 50
intervalo=(1,100)
comprobar_valor(valor,intervalo)