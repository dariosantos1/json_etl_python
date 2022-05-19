# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from socket import timeout
from flask_login import user_unauthorized
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    response = requests.get(url)
    data = response.json()
    
    user_1 =[data for d in data if d["completed"] == True and d["userId"] == 1]
    user_2 =[data for d in data if d["completed"] == True and d["userId"] == 2]
    user_3 =[data for d in data if d["completed"] == True and d["userId"] == 3]
    user_4 =[data for d in data if d["completed"] == True and d["userId"] == 4]
    user_5 =[data for d in data if d["completed"] == True and d["userId"] == 5]
    user_6 =[data for d in data if d["completed"] == True and d["userId"] == 6]
    user_7 =[data for d in data if d["completed"] == True and d["userId"] == 7]
    user_8 =[data for d in data if d["completed"] == True and d["userId"] == 8]
    user_9 =[data for d in data if d["completed"] == True and d["userId"] == 9]
    user_10 =[data for d in data if d["completed"] == True and d["userId"] == 10]

    print ("Usuario 1 : Completo" ,len(user_1),"Títulos")
    print ("Usuario 2 : Completo" ,len(user_2),"Títulos")
    print ("Usuario 3 : Completo" ,len(user_3),"Títulos")
    print ("Usuario 4 : Completo" ,len(user_4),"Títulos")
    print ("Usuario 5 : Completo" ,len(user_5),"Títulos")
    print ("Usuario 6 : Completo" ,len(user_6),"Títulos")
    print ("Usuario 7 : Completo" ,len(user_7),"Títulos")
    print ("Usuario 8 : Completo" ,len(user_8),"Títulos")
    print ("Usuario 9 : Completo" ,len(user_9),"Títulos")
    print ("Usuario 10 : Completo" ,len(user_10),"Títulos")

    titulos_completados = [len(user_1), len(user_2), len(user_3), len(user_4), len(user_5),len(user_6), len(user_7), len(user_8), len(user_9), len(user_10)]
    id_usuarios =["Usuario_1", "Usuario_2", "Usuario_3", "Usuario_4", "Usuario_5", "Usuario_6", "Usuario_7", "Usuario_8", "Usuario_9", "Usuario_10"]
    
    fig = plt.figure()
    fig.suptitle("Títulos Completados Por Usuario", fontsize=10)
    ax = fig.add_subplot()
    ax.bar(id_usuarios, titulos_completados, label="Usuarios")
    ax.set_facecolor ("orange")
    ax.legend ()
    plt.show()

    print("terminamos")