# SEMANA 16
# Trabajo con Archivos de Texto en Python
# Escritura de Archivo de Texto
# Abrir el archivo en modo lectura
ruta = "my_notes.txt"
mis_notas = open("my_notes.txt", "r")
# Leer el contenido del archivo línea por línea
lineas = mis_notas.readlines()
print(lineas)
# Cerrar el archivo
mis_notas.close()

# Otro método a utilizar
'''with open("my_notes.txt") as archivo:
    lineas = archivo.readlines()
    #print(lineas)

for l in lineas:
    print(l.replace("\n", ""))'''