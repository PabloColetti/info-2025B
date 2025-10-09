

# def saludo(nombre):
#     print(f"Hola {nombre}")

# saludo("Pablo")
# saludo("Nayla")
# saludo("Diego")

############

# notas_pedro = [10, 8, 4]
# total_notas_pedro = 0

# for nota in notas_pedro:
#     total_notas_pedro += nota

# promedio_pedro = total_notas_pedro / len(notas_pedro)

# print(f"Total: {total_notas_pedro}")
# print(f"Cantidad de notas_pedro: {len(notas_pedro)}")
# print(f"Promedio_pedro: {promedio_pedro}")

# notas_nayla = [10, 10, 10]
# total_notas_nayla = 0

# for nota in notas_nayla:
#     total_notas_nayla += nota

# promedio_nayla = total_notas_nayla / len(notas_nayla)

# print(f"Total: {total_notas_nayla}")
# print(f"Cantidad de notas_nayla: {len(notas_nayla)}")
# print(f"Promedio_nayla: {promedio_nayla}")

# estudiantes = [
#     {
#         "nombre": "Pedro",
#         "notas": {
#             "mate": {
#                 "parcial_1": 10,
#                 "parcial_2": 5,
#                 "parcial_3": 2,
#                 "nota_final": None
#             },
#             "literatura": {
#                 "parcial_1": 10,
#                 "parcial_2": 5,
#                 "parcial_3": 2,
#                 "nota_final": None
#             }
#         }
#     },
#     {
#         "nombre": "Nayla",
#         "notas": {
#             "mate": {
#                 "parcial_1": 10,
#                 "parcial_2": 5,
#                 "parcial_3": 2,
#                 "nota_final": None
#             },
#             "literatura": {
#                 "parcial_1": 10,
#                 "parcial_2": 5,
#                 "parcial_3": 2,
#                 "nota_final": None
#             }
#         }
#     },
# ]


# def promedio(items, precision=2):
#     # return sum(items) / len(items)
#     total = 0

#     for item in items:
#         total += item

#     return round(total / len(items), precision)


# print(f"Promedio de Pedro: {promedio([10, 8, 4], 4)}")
# print(f"Promedio de Nayla: {promedio([10, 10,9])}")
# print(f"Promedio de Pablo: {promedio([5, 4, 10])}")

# def resta(a, b):
#     resultado = a - b

#     return resultado

# calculo = resta(20, 5)
# print(calculo)

# def saludo(nombre, edad):
#   print(f"Hola {nombre}, tenes: {edad}")

# saludo("Pablo", 28)
# saludo(20, "Elias")

# def suma(a, b):
#     resultado = a + b
#     return resultado

# *args: Permite pasar a una funcion un numero indeterminado/dinamico de argumentos posicionales

# def suma(*args):
#     print(args)
#     print(type(args))

#     resultado = 0

#     for numero in args:
#         resultado += numero

#     return resultado


# calculo = suma(5, 25, 30)
# print(calculo)

# **kwargs: Permite pasar a una funcion un numero indeterminado/dinamico de argumentos nombrados (clave-valor | key-value)

# def ver_persona(**kwargs):
# print(kwargs)
# print(type(kwargs))

# for key, value in kwargs.items():
#     print(f"Clave: {key} - Valor: {value}")


# {
#     'nombre': 'Pablo',
#     'edad': 28,
#     'altura': 1.75,
#     'materias': ['PW', 'DA']
# }
# ver_persona(nombre="Pablo", edad=28, altura=1.75, materias=["PW", "DA"])

#            posicionales
def funcion(a, b=1, *args, c, d=2, **kwargs):
#                        |      nombrados
    print("Parametros posicionales (positional / keyword)")
    print(f"a: {a}")
    print(f"b: {b}")

    print("Parametros posicionales indefinido/indeterminados/dinamicos (*args)")
    print(f"args: {args}")

    print("Parametros nombrados (keyword-only)")
    print(f"c: {c}")
    print(f"d: {d}")

    print("Parametros nombrados indefinido/indeterminados/dinamicos (*kwargs)")
    print(f"kwargs: {kwargs}")


funcion(20, 5, "otro_posicional", "otro_posicional_2",
        "otro_posicional_3", c=30, d=True, algo="algomas", algo2="algomas2")
