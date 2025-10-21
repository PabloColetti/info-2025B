from carpeta_a.modulo_aa import saludar_con_nombre_de_funcion_largo as saludo
from carpeta_a.modulo_ab import despedir

def saludo_despida():
  mensaje_saludo = saludo("Pablo")
  print(mensaje_saludo)
  
  mensaje_despedida = despedir("Pablo")
  print(mensaje_despedida)