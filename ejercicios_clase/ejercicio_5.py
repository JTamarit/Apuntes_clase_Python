diccionario={}
numero_claves=10
clave=1
while clave <= numero_claves:
    valor= clave * clave
    diccionario[clave]=valor
    clave += 1
print(f"\n El diccionario con {numero_claves} claves es: {diccionario})\n")

