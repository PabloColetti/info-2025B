print("##### STRINGS INTRO A F-STRINGS #####")

nombre = "Pepe"
apellido = "Fulanito"

mensaje = f"Hola {nombre}, {apellido}"
print(mensaje)

mensaje_dos = "Hola {}, {}".format(apellido, nombre)
print(mensaje_dos)

num_1 = 5
num_2 = 10

mensaje_tres = f"La suma de {num_1} + {num_2} es igual a {num_1 + num_2}"
print(mensaje_tres)

mensaje_tres = f"La suma de {num_1} + {num_2}:\n{num_1 + num_2}"
print(mensaje_tres)

cadena = "Hola info | "
cadena_repetida = cadena * 2
print(cadena_repetida)

texto = "cinco"
longitud = len(texto)
print(type(texto))
print(longitud)

# slicing
#            123456789
texto_dos = "Hola Info 🚀"
subcadena = texto_dos[5:9]
print(subcadena)

cadena_invertida = texto_dos[::-1]
print(cadena_invertida)

cadena_mayusculas = texto_dos.upper()
print(cadena_mayusculas)

cadena_minusculas = texto_dos.lower()
print(cadena_minusculas)

nombre_dos = "diego oscar"
cadena_capitalizada = nombre_dos.capitalize()
print(cadena_capitalizada)

cadena_tabulada = "\tHola\tinfo"
print(cadena_tabulada)

comillas_escapadas = "en el 'caso' tal cosa"
print(comillas_escapadas)

comillas_escapadas = "en el \"caso\" tal cosa"
print(comillas_escapadas)