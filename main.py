
def eliminar_estudiante(id):
    estudiantes = leer_estudiantes()
    estudiante = next((e for e in estudiantes if e['id'] == id), None)

    if not estudiante:
        print("❌ No existe un estudiante con ese ID.")
        return

    estudiantes.remove(estudiante)
    guardar_estudiantes(estudiantes)
    print(f"✔ Estudiante con ID {id} fue eliminado.")