def contar(cadena):
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

    p_max = max(dic_frecuencia.items())
    return tuple(p_max)


print("Función para identificar la palabra con mayor frecuencia")
cadena = str(input("Ingrese un texto: "))

print(contar(cadena))
