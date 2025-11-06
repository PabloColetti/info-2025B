import sqlite3
import datetime
import uuid

conn = sqlite3.connect('new-blog.db')

cursor = conn.cursor()


def crear_tablas():
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                  id VARCHAR PRIMARY KEY,
                  username VARCHAR UNIQUE NOT NULL,
                  email VARCHAR UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  created_at TEXT NOT_NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS posts (
                  id VARCHAR PRIMARY KEY,
                  usuario_id VARCHAR NOT NULL,
                  titulo TEXT NOT NULL,
                  contenido TEXT NOT NULL,
                  created_at TEXT NOT_NULL,
                  FOREIGN KEY (usuario_id) REFERENCES usuarios(id))''')


def crear_usuario():
    # solicitar lo necesario
    # validamos y sanitizamos "Pablo"
    # procesamos
    # ejecutamos sql
    pass


def crear_post():
    pass


def cerrar_conexion():
    cursor.close()
    conn.close()


def menu():
    crear_tablas()
    while True:
        # CRUD -> CREATE - READ - UPDATE - DELETE
        print("--- MENU ---")
        print("1. Crear usuario")
        print("2. Crear post")
        print("3. Crear comentario")
        print("4. Crear categoria")
        print("5. Listar usuario")
        print("6. Listar post")
        print("7. Listar comentario")
        print("8. Listar categoria")
        print("9. Actualizar usuario")
        print("10. Actualizar post")
        print("11. Actualizar comentario")
        print("12. Actualizar categoria")
        print("13. Eliminar usuario")
        print("14. Eliminar post")
        print("15. Eliminar comentario")
        print("16. Eliminar categoria")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if (opcion == '1'):
            crear_usuario()
        elif (opcion == '2'):
            crear_post()
        elif (opcion == "0"):
            cerrar_conexion()
            break
        else:
            print("Opcion no valida")


menu()
