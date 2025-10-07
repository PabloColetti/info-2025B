print("##### OPERADORES TERNARIOS #####")

# resultado = True ? "Verdadero" : "Falso"

a = 10
b = 30

resultado = "a es mayor que b" if a > b else "b es mayor que a"
print(f"Operador ternario: {resultado}")

if a > b:
    resultado = "a es mayor que b"
else:
    resultado = "b es mayor que a"
