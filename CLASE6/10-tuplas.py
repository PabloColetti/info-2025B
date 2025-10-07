print("##### LISTAS #####")

# Se definen entre parentesis, son ordenadas (elementos tienen indice)
# Son inmutables (no se puede agregar, modificar y eliminar)

#           0           1             2
tupla = ("manzanas", "naranjas", "frutillas", "duraznos")
print(f"valor: {tupla}, tipo: {type(tupla)}")

print(f"Primer elemento: {tupla[0]}")
print(f"Ultimo elemento: {tupla[-1]}")

print(f"Longitud de la tupla: {len(tupla)}")

print(f"Veces que aparece el 'frutillas': {tupla.count("frutillas")}")

print(f"El indice de 'naranjas': {tupla.index("naranjas")}")

a, b, c = tupla
print(f"Desempaquetado a={a}, b={b}, c={c}")

primer_elem, *resto = tupla
print(f"Desempaquetado Primero = {primer_elem}, Resto = {resto}")

