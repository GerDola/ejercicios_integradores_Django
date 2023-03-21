import re


class Persona():
    def __init__(self, nombre="", edad="", dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    @nombre.setter
    def nombre(self, valor):
        while True:
            if (re.search("[a-zA-Z|ñÑ ]", valor) is not None):
                self.__nombre = valor.capitalize()
                return print('Nombre cargado correctamente')
            else:
                self.__nombre = ""
                return print('Error al cargar el nombre')

    @edad.setter
    def edad(self, valor):
        try:
            if int(valor) >= 0 and int(valor) < 100:
                self.__edad = valor
                return print('Edad Ingresada correctamente')
            else:
                self.__edad = ""
                return print('Ingrese Edad de 1 a 100')
        except ValueError:
            self.__edad = ""
            return print('Error en ingreso de edad. Introduzca números.')

    @dni.setter
    def dni(self, valor):
        try:
            if len(valor) < 9 and len(valor) > 6:
                valor = int(valor)
                self.__dni = valor
                return print('DNI cargado correctamente')
            else:
                self.__dni = ""
                return print('El DNI solo debe contener de 7 a 8 números sin puntos.')
        except ValueError:
            self.__dni = ""
            return print('Error al cargar el DNI. Ingrese un número válido')

    def es_mayor_de_edad(Persona):
        try:
            if int(Persona.edad) >= 18:
                return True
            else:
                return False
        except ValueError:
            return print('La Edad se ingresó incorrectamente. Corrija para saber si es menor o mayor')

    def mostrar(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}'


class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular(Persona)
        self.cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self, valor):
        self.__titular = valor

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        return f"Datos de la Cuenta:\nTitular: {self.titular}\nCantidad en cuenta: $ {str(self.cantidad)}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad


persona = Persona('german', 33, 12345678)

cuenta = Cuenta(Persona, 2000)
print(cuenta.mostrar())

deposito = 1000
cuenta.ingresar(deposito)
print(cuenta.mostrar())

extraccion = 3000
cuenta.retirar(extraccion)
print(cuenta.mostrar())
