# import pyautogui as pg
# import time

# # boton OK 1013,685
# # while(1):
# #     print(pg.position())
# # time.sleep(5)

# time.sleep(2)
# pg.doubleClick(938,540)
# pg.typewrite("hola")
# print(pg.position())       
# pg.click(1013,685)     
# while(1):
import itertools,time

# Define los caracteres permitidos para la clave
caracteres = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Define la longitud mínima y máxima de la clave
longitud_minima = 4
longitud_maxima = 8

tiempo_inicio = time.time()

# Crea una lista de todas las posibles combinaciones de claves
combinaciones = []
for longitud in range(longitud_minima, longitud_maxima+1):
    for combinacion in itertools.product(caracteres, repeat=longitud):
        clave = ''.join(combinacion)
        print(clave)

tiempo_fin = time.time()
duracion = tiempo_fin - tiempo_inicio

print(f"El programa tardó {duracion:.4f} segundos en ejecutarse.")