def edad(valor):
    if type(valor) != int:
        try:
            valor = int(valor)
            return valor
        except ValueError:
            while True:
                return edad(input('ingrese un valor correcto: '))


valor = input('ingrese un valor: ')

print(edad(valor))
