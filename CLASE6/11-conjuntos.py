# Los conjuntos se definene entre llaves {}
# No permiten elementos duplicados
# No son ordenados (no tienen indice)
# Son mutables (se pueden modificar, agregar, eliminar elementos)

colores = {"rojo", "verde", "azul"}
print(f"valor: {colores}, tipo: {type(colores)}")

colores.add("amarillo")
print(f"Conjunto despues del add: {colores}")

colores.remove("verde")
print(f"Conjunto despues del remove: {colores}")

colores.discard("naranja")
print(f"Conjunto despues del discard: {colores}")

conjunto = {"hola info", True, 42, (1, 2)}