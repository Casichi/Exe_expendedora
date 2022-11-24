import csv
import pandas as pd
import numpy as np
import re

lett_patter = '^[A-Za-z]+$'
num_patter = '^[0-9]+$'

print("productos disponibles")

# La funcion de abrir cualquier documento es una funcion de transaccion y control de concurrencia
producto = pd.read_csv('DB_CSV.csv')
np_array = np.array(producto)
print(np_array)


while True:
    introducir_dinero = input("introduzca dinero ")
    if re.fullmatch(num_patter, (introducir_dinero)):
        break

while True:
    introducir_datos = input("que desea comprar?")
    if re.fullmatch(num_patter, introducir_datos):
        break

with open('DB_CSV.csv', newline='', mode='r+') as db:
    lector = csv.reader(db, delimiter=',')
    linea = lector.line_num

    for row in lector:
        introducir_datos_int = (int(introducir_datos))
        if str(introducir_datos_int) in row[0]:
            stock = int(row[3])
            if stock <= 0:
                print("No hay Articulo Disponible, Seleccione Otro")
                break
            else:
                print(f' Producto seleccionado cuesta {row[2]} e introdujo {introducir_dinero}')
                if int(introducir_dinero) >= int(row[2]):
                    remain = stock - 1
                    devuelta = int(introducir_dinero) - int(row[2])
                    print(f'su producto {row[1]} esta disponible, su cambio es {devuelta} ')
                    np_array[int(introducir_datos) - 1, 3] = remain
                    np_array = np_array
                    print(np_array)
                    break
                elif int(introducir_dinero) < int(row[2]):
                    print("Dinero insuficiente")
                    break
    else:
        print("Producto no encontrado")
np.savetxt('DB_CSV.csv', np_array, delimiter=",", fmt="%s", header="Codigo,Producto,Precio,Stock")