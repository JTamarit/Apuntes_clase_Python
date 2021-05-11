lista_numeros=list(range(10))
lista_pares=lista_numeros.copy()
lista_pares.remove(1)
lista_pares.remove(3)
lista_pares.remove(5)
lista_pares.remove(7)
lista_pares.remove(9)
print(f"La lista de los números pares del 0 al 9 es: {lista_pares}")

'''
Una solución más directa podría haber sido:
lista_pares=list(range(0,10,2))
print(lista_pares)
'''
