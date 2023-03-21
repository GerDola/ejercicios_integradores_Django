class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def ingresar(self, titular):
        Ejecutable.ingresar(titular)

    def retirar(self, titular):
        Ejecutable.retirar(titular)


class Ejecutable():

    def ingresar(titular):
        # nombre = titular
        print(f"¿{titular} cuanto es la cantidad que quiere depositar a su cuenta?")
        cantidad = int(input())
        print(f"Se han agregado ${cantidad} a su cuenta.")
        print(f"¿{titular} le gustaria hacer otra cosa? [S]/[N]")
        opcion = input()
        if opcion == "S":
            menu(titular)
        else:
            print(f"Gracias por su visita {titular}")
            exit()

    def retirar(titular):
        cantidad = 1000
        print(f"¿{titular} cuanto es la cantidad que quiere retirar de su cuenta?")
        cantidad_retirar = int(input())
        if cantidad >= cantidad_retirar:
            retiro = cantidad - cantidad_retirar
            print(
                f"{titular} ha retirado {cantidad_retirar} de su cuenta y le queda un saldo de {retiro}.")
            print("Gracias por visitarnos")
        else:
            print("No cuenta con el saldo suficiente.")


def menu(titular):
    instancia = Cuenta(titular)
    print("¿Quiere [R]etirar o [I]ngresar efectivo?")
    accion = input()
    if accion == "R":
        instancia.retirar(titular)
    elif accion == "I":
        instancia.ingresar(titular)
    else:
        print(f"Opcion incorrecta {titular}, gracias por visitarnos.")


def main():
    print("¿Cual es su nombre?")
    titular = input()
    print(f"Me alegro de conocerle, {titular} y sera un placer atenderle")
    menu(titular)


if __name__ == "__main__":
    main()
