import sqlite3
import os
from tabulate import tabulate



def verificar(texto):
    while texto == "":
        print("Error, campo vacio")
        texto = input("Ingrese texto nuevamente: ")
    return texto

def input_numerico(frase):
    valor = input(frase)
    while True:
        try:
            valor = int(valor)
            break
        except ValueError:
            print("ERORR SOLO ENTEROS")
        valor = input("Ingrese nuevamente : " + frase)
    return valor    


def insertar(i,nom,prec):
    conn = sqlite3.connect("local.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("CREATE TABLE productos (id INT, nombre TEXT, precio INT)")
    except sqlite3.OperationalError:
        print("YA EXISTE LA TABLA ") 
    cursor.execute("INSERT INTO productos VALUES (?,?,?)", (i,nom,prec))
    conn.commit()
    conn.close()
    print("Productos salvado con exito ! ")


def mostrar():
    conn = sqlite3.connect("local.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    return datos



while True:
    print("""
      1) Insetar productos : 
      2) Ver productos : 
      3) Salir.
      """)
    opcion = input(">>>")
    if opcion == "1": 
        nombre = input("Ingrese nombre de producto : ")
        nombre = verificar(nombre)
        idi = input_numerico("Ingrese ID del producto: ")
        precio = input_numerico("Ingrese precio del producto: ")
        insertar(idi,nombre,precio)
    elif opcion == "2":
        r = mostrar()
        print(tabulate(r,["ID","NOMBRE","PRECIO"],tablefmt="pretty"))
    elif opcion == "3" :
        print("Gracias por utlizar nuestro programa! ")
        break
    else: print("Error de opcion !")

    input("Toque ENTER para continuar...")
    os.system("cls")



         

    


