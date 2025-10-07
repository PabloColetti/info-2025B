# Los diccionarios se definene entre llaves {}
# Estan compuestos con clave-valor (key-value)
# Son desordenados, no poseen indice sino que que se acceden a sus elementos medidante la clave

# nombre = input("Ingresa el nombre: ")
# edad = int(input("Ingresa la edad: "))
# altura = float(input("Ingresa la edad: "))

estudiante = {
    # "nombre": nombre,
    # "edad": edad,
    # "altura": altura,
    "nombre": "Ana",
    "edad": 15,
    "altura": 1.65,
    "cursos": {
        "programacion": {
            "profesor": "Romero",
            "horario": [
              "8:00",
              "10:00"
            ]
        },
        "diseño": {
            "profesor": "Elias",
            "horario": [
              "10:00",
              "12:00"
            ]
        }
    }
}

print(f"valor: {estudiante}, tipo: {type(estudiante)}")

print(f"El nombre es: {estudiante["nombre"]}")
print(f"Los cursos en los que esta son: {estudiante["cursos"]}")
print(f"El horario del curso de diseño es: {estudiante["cursos"]["diseño"]["horario"]}")
print(f"La hora de inicio del curso de diseño es: {estudiante["cursos"]["diseño"]["horario"][0]}")
print(f"La hora de final del curso de diseño es: {estudiante["cursos"]["diseño"]["horario"][1]}")
print(f"El profe del curso de diseño es: {estudiante["cursos"]["diseño"]["profesor"]}")

print("##### METODOS #####")

print(f"Claves del diccionario: {list(estudiante.keys())}")
print(f"Valores del diccionario: {list(estudiante.values())}")
print(f"Items del diccionario: {list(estudiante.items())}")

