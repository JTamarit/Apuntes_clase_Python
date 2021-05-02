lista_palabras = ['arbol','almendra','alhacenas', 'almendrado', 'azucarados', 'coche', 'almacenados']
contador=0

for palabra in lista_palabras:
    
   if palabra.startswith('a') and len(palabra)>10:
       print("\n PALABRA ENCONTRADA\n")
       print(f"\n La palabra es: {palabra}\n")
       break
   else: 
       contador +=1
       continue
if contador == len(lista_palabras):
    print("PALABRA NO ENCONTRADA")

    