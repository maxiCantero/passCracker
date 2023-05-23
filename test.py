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
longitud_minima = 7
longitud_maxima = 8

inicio = 17411600
tiempo_inicio = time.time()
datos_recibidos = b""
caracter_parada = b"<"
# # Crea una lista de todas las posibles combinaciones de claves
clave_encontrada = False
combinaciones = []
for longitud in range(longitud_minima, longitud_maxima+1):
    rango_inicio = inicio - 10 ** (longitud - 1)  # Calcula el rango de inicio según la longitud de la clave
    rango_fin = inicio + 10 ** (longitud - 1)  # Calcula el rango de fin según la longitud de la clave
    for num in range(rango_inicio, rango_fin):
        
        clave = str(num)
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
        
        if clave_encontrada == True:
            print("Esta es la clave del equipo",clave)
            break
        
    if clave_encontrada == True:
        break

tiempo_fin = time.time()
duracion = tiempo_fin - tiempo_inicio

print(f"El programa tardó {duracion:.4f} segundos en ejecutarse.")