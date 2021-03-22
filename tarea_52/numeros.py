from estructura_numeros import EstructuraNumeros

estructura = EstructuraNumeros()


def muestra_menu_lista(lista):
    print(f"La lista es  =  {lista}")
    opcion = int(input(f"""
    Elige tu opción:
    1- Eliminar primera ocurrencia de un número
    2 - Recorrer la lista para imprimir la sumatoria de todos los elementos.
    3 - Crear una lista eliminando los elementos que sean mayores que un número
    4 - Ocurrencias de la lista
    5 - Añadir nuevo número
    6 - Restaurar lista original ({lista_original})
    0 - Salir
    """))
    return opcion


def menu_inicio():
    lista = estructura.crea_lista()
    numero = int(
        input("Introduce numero a añadir a la estructura, 0 para continuar:\n"))
    while not (numero == 0):
        lista = estructura.insertar(lista, numero)
        numero = int(
            input("Introduce numero a añadir a la estructura, 0 para continuar:\n"))
    return lista


lista = menu_inicio()
lista_original = estructura.crea_lista(lista)

opcion = muestra_menu_lista(lista)
while not (opcion == 0):
    if opcion == 1:
        # eliminar
        numero = int(
            input("Introduce numero a eliminar:\n"))
        lista = estructura.eliminar_si_existe(lista, numero)
    elif opcion == 2:
        # sumatorio
        sumatorio = estructura.sumatorio(lista)
        print(f"La suma de los elementos es   =  {sumatorio}")
    elif opcion == 3:
        # lista con menores
        numero = int(
            input("Introduce numero a comparar:\n"))
        lista = estructura.eliminar_mayores(lista, numero)
    elif opcion == 4:
        # ocurrencias
        ocurrencias = estructura.numero_ocurrencias(lista)
        print(f"Las ocurrencias son (numero,ocuurencias)   =  {ocurrencias}")
    elif opcion == 5:
        # añadir
        numero = int(
            input("Introduce numero a añadir a la estructura:\n"))
        lista = estructura.insertar(lista, numero)
    elif opcion == 6:
        # restaurar
        lista = estructura.crea_lista(lista_original)
    else:
        # opcion no reconocida
        print(f"Opción {opcion} desconocida, vuelve a intentarlo")
    opcion = muestra_menu_lista(lista)
