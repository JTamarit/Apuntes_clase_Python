lista_con_duplicados=[1,2,3,4,4,4,5,5,6,7,8,8,9,9,10,11,12,12]
longitud_lista_duplicados=len(lista_con_duplicados)
lista_sin_duplicados=[]
elementos_duplicados=[]
for elemento in lista_con_duplicados:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
    else: elementos_duplicados.append(elemento)
longitud_lista_no_duplicados=len(lista_sin_duplicados)
print(f"\n La lista con duplicados tiene {longitud_lista_duplicados} elmentos: {lista_con_duplicados}")
print(f"\n La lista sin duplicados tiene {longitud_lista_no_duplicados} elementos: {lista_sin_duplicados}")
print(f"\n Los elementos duplicados son: {elementos_duplicados}\n")

