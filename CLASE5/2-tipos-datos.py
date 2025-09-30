print("##### DATOS PRIMITIVOS #####")

nombre = "Juan"
print(f"valor: {nombre}, tipo: {type(nombre)}")

edad = 21
print(f"valor: {edad}, tipo: {type(edad)}")

altura = 1.75
print(f"valor: {altura}, tipo: {type(altura)}")

es_estudiante = True
print(f"valor: {es_estudiante}, tipo: {type(es_estudiante)}")

complejo = complex(2, 3)
print(f"valor: {complejo}, tipo: {type(complejo)}")

print("##### ESTRUCTURAS DE DATOS #####")

lista = ["manzana", "naranja", "frutilla", True, 15, [12.5, 5.5]]
print(f"valor: {lista}, tipo: {type(lista)}")

tupla = ("manzana", "naranja", "frutilla")
print(f"valor: {tupla}, tipo: {type(tupla)}")

set_mio = {"manzana", "naranja", "frutilla"}
print(f"valor: {set_mio}, tipo: {type(set_mio)}")

diccionario = {"nombre": "Ana", "edad": 35, "altura": 1.68}
print(f"valor: {diccionario}, tipo: {type(diccionario)}")
