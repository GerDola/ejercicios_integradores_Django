def mcm(a, b):
    i = max(a, b)

    while True:
        if (i % a == 0) and (i % b == 0):
            return i

        i += 1


print("Función de cálculo de mínimo común múltiplo (MCM)")

a = int(input("Ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))

print(f"El mínimo común múltiplo de {a} y {b} es: {mcm(a, b)}")
