# while True:
# print("Hola Info 🚀") # para deterlo al bucle infinito CTRL + C (en la terminal)


estudiantes = []

# bandera = True
while True:

    respuesta = input("Desea continuar? (S/N) o X: ")

    if respuesta == "S":
        print("Continuamos")

        nombre = input("Ingresa el nombre del estudiante: ")
        edad = input("Ingresa la edad del estudiante: ")

        estudiantes.append({
            "nombre": nombre,
            "edad": edad
        })

    elif respuesta == "N":
        print("Chau!")
        # bandera = False
        break

    elif respuesta == "X":
        print("Presionaste x")
        continue

    else:
        print("Valor invalido")

print(f"Estudiantes registrados {estudiantes}")
