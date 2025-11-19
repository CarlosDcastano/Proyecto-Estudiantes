
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

