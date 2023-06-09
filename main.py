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
import itertools,time, serial
import serial.tools.list_ports

puertos_disponibles = serial.tools.list_ports.comports()
for puertos in puertos_disponibles:
    print(puertos.device)

puerto_seleccionado = input("seleccione el puerto: ")
velocidad = 19200
ser = serial.Serial(puerto_seleccionado,velocidad)

if ser.isOpen():
    print("Puerto",puerto_seleccionado,"abierto.")

# datos_recibidos = ser.read()

# print(datos_recibidos)

# Define los caracteres permitidos para la clave
caracteres = '0123456789'
# # Define la longitud mínima y máxima de la clave
longitud_minima = 1
longitud_maxima = 8

dato_correcto = "1111"
tiempo_inicio = time.time()
datos_recibidos = b""
caracter_parada = b"<"
# # Crea una lista de todas las posibles combinaciones de claves
clave_encontrada = False
combinaciones = []
for longitud in range(longitud_minima, longitud_maxima+1):
    for combinacion in itertools.product(caracteres, repeat=longitud):
        clave = ''.join(combinacion)
        datos = ">SPW"+clave+"<"
        ser.write(datos.encode())
        print(clave)
        while True:
            dato = ser.read()
            datos_recibidos += dato
            if dato == caracter_parada:
                # print(datos_recibidos)
                if datos_recibidos != b">RPW;*7A<":
                    clave_encontrada = True
                 
                datos_recibidos = b""
                break
        # print(clave_encontrada)
        if clave_encontrada == True:
            print("Esta es la clave del equipo",clave)
            break
        # print(ser.read(10))
        # print(type(clave))
    if clave_encontrada == True:
        break
tiempo_fin = time.time()
duracion = tiempo_fin - tiempo_inicio

print(f"El programa tardó {duracion:.4f} segundos en ejecutarse.")