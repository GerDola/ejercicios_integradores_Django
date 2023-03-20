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
            #valor = int(valor)
            if int(valor) > 0 and int(valor) < 100:
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


nombre = input('Ingrese el Nombre: ')
edad = input('Ingrese la Edad: ')
dni = input('Ingrese el DNI: ')

a = Persona(nombre, edad, dni)

print(a.mostrar())
print(a.es_mayor_de_edad())
