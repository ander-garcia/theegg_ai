from persona import Persona
from cuenta import Cuenta

ander = Persona("ander", 41, "11111111H")
ander.mostrar()

ander.nombre = "1231"
ander.edad = -1
ander.dni = "asadasd"

ander.nombre = "ander"
ander.edad = 41
ander.mostrar()

cuenta = Cuenta(ander, 100)
cuenta.mostrar()

cuenta.ingresar(100)
cuenta.mostrar()

cuenta.retirar(150)
cuenta.mostrar()
cuenta.retirar(150)
cuenta.mostrar()
