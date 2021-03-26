class Cuenta():

    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f" Cantidad : {self.cantidad} \n Titular:")
        self.titular.mostrar()

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        else:
            print("Cantidad incorrecta")

    def retirar(self, cantidad):

        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad
            if self.cantidad < 0:
                print(
                    f"CUIDADO estás en números rojos, tu saldo es de {self.cantidad}")
        else:
            print("Cantidad incorrecta")
