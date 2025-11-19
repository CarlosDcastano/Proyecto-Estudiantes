import json                  #importa la libreria json en python para exportar los archivos 
import csv                   #importa la libreria csv para exportar los estudiantes 

# --------------------------
#  LECTURA Y ESCRITURA JSON
# --------------------------
def leer_estudiantes():                                      
    """Lee los estudiantes desde el archivo JSON."""
    try:
        with open('estudiantes.json', 'r') as archivo:     # Abre el archivo estudiantes.json en modo lectura ('r'). La palabra with garantiza que el archivo se cierre automáticamente después de leerlo.
            estudiantes = json.load(archivo)               # Carga los datos del archivo JSON en una variable (el .load convierte los datos del usuario en una lista)
        return estudiantes                                 # Devuelve la lista de estudiantes cargada desde el archivo. 
    except FileNotFoundError:                              # Si el archivo estudiantes.json no existe, el código maneja este error y devuelve una lista vacía [] para que el programa siga funcionando.
        return []                                          # Si el archivo no existe, devuelve una lista vacía


def guardar_estudiantes(estudiantes):                                          
    """Guarda la lista de estudiantes en el archivo JSON."""
    with open('estudiantes.json', 'w') as archivo:                      #Abre el archivo estudiantes.json en modo escritura ('w'). Si el archivo ya existe, se sobrescribe.
        json.dump(estudiantes, archivo, indent=4)                       #La función json.dump() convierte la lista estudiantes a formato JSON y la guarda en el archivo. El argumento indent=4 es para que aparezca un dato debajo de otro.

#Correcciones hechas.