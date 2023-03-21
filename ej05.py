def get_int(a):
    try:
        return int(a)
    except ValueError:
        while True:
            return get_int(input("No ingresó un número entero. Vuelva a intentar: "))


a = input("Ingrese un numero entero: ")
print(get_int(a))
