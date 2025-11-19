
import json
import csv

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

# --------------------------
#          CRUD
# --------------------------

def crear_estudiante(nombre, edad, curso):                                # Define la función crear_estudiante que toma tres parámetros: el nombre, edad y curso del estudiante que vamos a agregar
    estudiantes = leer_estudiantes()                                      # Llama a la función leer_estudiantes() para cargar la lista de estudiantes actuales desde el archivo.
    nuevo_id = max([e['id'] for e in estudiantes], default=0) + 1         # Genera un nuevo id único para el estudiante. Usa el valor más alto de los IDs existentes, le suma 1, y si la lista está vacía (no hay estudiantes), usa el valor 0 como base. Esto asegura que los IDs sean secuenciales.

    nuevo_estudiante = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "curso": curso
    }

    estudiantes.append(nuevo_estudiante)
    guardar_estudiantes(estudiantes)
    print(f"✔ Estudiante '{nombre}' agregado con ID {nuevo_id}.")


def actualizar_estudiante(id, nombre=None, edad=None, curso=None):
    if not estudiante:
        print("No existe un estudiante con ese ID.")
        return
    if nombre:
        estudiante["nombre"] = nombre
    if edad:
        estudiante["edad"] = edad
    if curso:
        estudiante["curso"] = curso

    guardar_estudiantes(estudiantes)
    print(f"✔ Estudiante con ID {id} actualizado.")

def eliminar_estudiante(id):
    estudiantes = leer_estudiantes()
    estudiante = next((e for e in estudiantes if e['id'] == id), None)

    if not estudiante:
        print("No existe un estudiante con ese ID.")
        return

    estudiantes.remove(estudiante)
    guardar_estudiantes(estudiantes)
    print(f"✔ Estudiante con ID {id} fue eliminado.")

def mostrar_estudiantes():
    estudiantes = leer_estudiantes()

    if not estudiantes:
        print("⚠ No hay estudiantes registrados.")
        return

    print("\n--- LISTA DE ESTUDIANTES ---")
    for est in estudiantes:
        print(f"ID: {est['id']} | Nombre: {est['nombre']} | Edad: {est['edad']} | Curso: {est['curso']}")
    print("-----------------------------")


# --------------------------
#      EXPORTAR A CSV
# --------------------------
def exportar_csv():                                 # esta función exporta los datos del JSON a un archivo CSV
    estudiantes = leer_estudiantes()

    if not estudiantes:
        print("⚠ No hay estudiantes para exportar.")
        return

    with open('estudiantes.csv', 'w', newline='') as archivo:      # abre el archivo estudiantes.csv en modo escritura
        escritor = csv.writer(archivo)                              # crea un escritor CSV

        escritor.writerow(["id", "nombre", "edad", "curso"])       # escribe los encabezados del archivo csv

        for est in estudiantes:                                     # recorre cada estudiante
            escritor.writerow([est["id"], est["nombre"], est["edad"], est["curso"]])  # escribe cada estudiante en el csv

    print("✔ Archivo estudiantes.csv exportado correctamente.")     # mensaje al usuario



# --------------------------
#          MENÚ
# --------------------------
def mostrar_menu():
    print("""
=============================
   SISTEMA CRUD ESTUDIANTES  
=============================
1. Crear estudiante
2. Mostrar estudiantes
3. Actualizar estudiante
4. Eliminar estudiante
5. Exportar a CSV
6. Salir
""")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            curso = input("Curso: ")
            crear_estudiante(nombre, edad, curso)

        elif opcion == "2":
            mostrar_estudiantes()

        elif opcion == "3":
            id = int(input("ID del estudiante a actualizar: "))
            nombre = input("Nuevo nombre (enter para no cambiar): ")
            edad = input("Nueva edad (enter para no cambiar): ")
            curso = input("Nuevo curso (enter para no cambiar): ")

            actualizar_estudiante(
                id,
                nombre if nombre else None,
                int(edad) if edad else None,
                curso if curso else None
            )

        elif opcion == "4":
            id = int(input("ID a eliminar: "))
            eliminar_estudiante(id)

        elif opcion == "5":
            exportar_csv()

        elif opcion == "6":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta otra vez.")


if __name__ == "__main__":
    main()

#Cambios by Isa Palacios

