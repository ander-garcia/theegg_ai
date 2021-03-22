from estructura_nombres import EstructuraNombres


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
