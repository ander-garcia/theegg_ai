class Persona():

    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        nombre_valido = True
        caracteres_no_alfanumericos = ''.join(
            [i for i in nombre if not i.isalpha()])
        if len(caracteres_no_alfanumericos) > 0:
            print("Nombre incorrecta, no puede contener caracteres no alfanuméricos")
        elif len(nombre) == 0:
            print("El nombre no puede estar vacio")
        else:
            self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if (int(edad) >= 0 and int(edad) < 150):
            self.__edad = edad
        else:
            print("Edad incorrecta, debe ser un número entre 0 y 150")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if self.is_dni_valido(dni):
            self.__dni = dni
        else:
            print("DNI invalido, compruebe letra y formato (ejemplo 12123123A)")

    def is_dni_valido(self, dni):
        # from https://discusionesconmipadre.wordpress.com/2010/10/19/comprobar-nif-con-python/
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        numeros = "1234567890"
        dni_valido = False
        if (len(dni) == 9):
            dni_letraControl = dni[8].upper()
            c = nif[:8]
            if (len(dni_numeros) == len([n for n in dni if n in numeros])):
                if tabla[int(dni_numeros) % 23] == dni_letraControl:
                    dni_valido = True
        return dni_valido

    def mostrar(self):
        print(f"{self.nombre}, {self.edad} años, DNI = {self.DNI}")

    def es_mayor_edad(self):
        return self.edad >= 18
