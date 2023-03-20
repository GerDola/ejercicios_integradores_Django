print("Programa para contar palabras y frecuencia")
cadena = str(input("Ingrese un texto: "))

remover = ".,:;¿?=/#%()&$\n¡!\"'"
for caracter in remover:
    cadena = cadena.replace(caracter, "")

cadena = cadena.lower()
palabras = cadena.split(" ")

dic_frecuencia = {}
for palabra in palabras:
    if palabra in dic_frecuencia:
        dic_frecuencia[palabra] += 1
    else:
        dic_frecuencia[palabra] = 1

print(dic_frecuencia)
