


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
    estudiantes = leer_estudiantes()
    estudiante = next((e for e in estudiantes if e['id'] == id), None)

    if not estudiante:
        print("❌ No existe un estudiante con ese ID.")
        return

    if nombre:
        estudiante["nombre"] = nombre
    if edad:
        estudiante["edad"] = edad
    if curso:
        estudiante["curso"] = curso

    guardar_estudiantes(estudiantes)
    print(f"✔ Estudiante con ID {id} actualizado.")
