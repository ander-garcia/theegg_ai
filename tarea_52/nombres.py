from estructura_nombres import EstructuraNombres


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


def menu_nombres():
    lista = []
    nombre = input("Introduce nombre a añadir , ?x? para continuar:\n")
    while not (nombre == "?x?"):
        lista.append(nombre)
        nombre = input("Introduce nombre a añadir , ?x? para continuar:\n")
    return lista


print("Nombres de pila de los alumnos de nivel primario \n")
print("----------------------")
primario = menu_nombres()
print(f"Todos los nombres de primario  {primario}")
print("----------------------")
print("")
print("Nombres de pila de los alumnos de nivel secundario \n")
print("----------------------")
secundario = menu_nombres()
print(f"Todos los nombres de secundario  {secundario}")
print("----------------------")
print("")
estructura = EstructuraNombres(primario)
nombres_todos = sorted(estructura.union_sin_duplicados(secundario))
nombres_comunes = sorted(estructura.interseccion(secundario))
nombres_solo_primario = sorted(
    estructura.diferentes_sin_duplicados(secundario))


print(
    f"Todos los nombres de primario y secundario sin duplicados {nombres_todos}")
print(f"Todos los nombres comunes sin duplicados  {nombres_comunes}")
print(
    f"Todos los nombres que sólo están en primario sin duplicados {nombres_solo_primario}")
