print("##### LISTAS #####")

# Se definen entre corchetes, son ordenadas (elementos tienen indice)
# Son mutables (agregar, modificar y eliminar)

#          0     1    2     3 ...
lista = ["info", 10, 1.75, True]
print(f"valor: {lista}, tipo: {type(lista)}")

#                     -1
#          0  1  2  3  4
numeros = [1, 2, 3, 4, 5, 3, "info", "info"]
print(f"Primer elemento: {numeros[0]}")
print(f"Ultimo elemento: {numeros[-1]}")

# slicing
print(f"Primeros 3 elementos: {numeros[:3]}")
print(f"Ultimos 2 elementos: {numeros[-2:]}")
print(f"Ultimos 2 elementos: {numeros[1:-1]}")

print(f"Longitud de la lista: {len(numeros)}")

print(f"Veces que aparece el 'info': {numeros.count("info")}")

numeros.append("algo")
print(f"Despues de agregar: {numeros}")

numeros[0] = True
print(f"Despues de modificar: {numeros}")

numeros.pop()
print(f"Despues de eliminar (pop): {numeros}")

numeros.remove(3)
print(f"Despues de eliminar (remove): {numeros}")


matriz = [
    #  0  1  2
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9]  # 2
]

print(f"Elemento en [1][0] {matriz[1][0]}")
