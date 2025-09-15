import csv
from datetime import datetime
from models import Client, SERVICIOS, PRIORIDADES

def seleccionar_opcion(lista, titulo):
    print(f"\nSeleccione {titulo}:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")
    while True:
        try:
            opcion = int(input(f"Ingrese el número de {titulo.lower()}: "))
            if 1 <= opcion <= len(lista):
                return lista[opcion - 1]
            else:
                print("Opción no válida.")
        except ValueError:
            print("Debe ingresar un número.")
def ingresar_clientes():
    clientes = []
    ids_usados = set()  # ✅ Guardar IDs únicos
    n = int(input("¿Cuántos pacientes desea ingresar? "))
    for i in range(n):
        print(f"\nPaciente {i+1}:")
        while True:
            try:
                id_p = int(input("ID (solo números): "))
                if id_p in ids_usados:
                    print("Ese ID ya está registrado. Ingrese uno diferente.")
                else:
                    ids_usados.add(id_p)
                    break
            except ValueError:
                print("El ID debe ser un número.")
        nombre = input("Nombre: ")
        servicio = seleccionar_opcion(SERVICIOS, "el servicio")
        prioridad = seleccionar_opcion(PRIORIDADES, "la prioridad")
        # Validación de fecha
        while True:
            fecha_str = input("Fecha y hora (YYYY-MM-DD HH:MM): ")
            formatos = ["%Y-%m-%d %H:%M", "%Y-%m-%d-%H:%M"]
            fecha = None
            for fmt in formatos:
                try:
                    fecha = datetime.strptime(fecha_str, fmt)
                    break
                except ValueError:
                    continue
            if fecha:
                break
            print("Formato inválido. Ejemplo: 2025-12-12 10:30")
        notas = input("Notas (opcional): ")
        clientes.append(Client(id_p, nombre, servicio, prioridad, fecha, notas))
    return clientes
def exportar_csv(nombre_archivo, lista_clientes):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nombre", "Servicio", "Prioridad", "Fecha", "Notas"])
        for c in lista_clientes:
            writer.writerow([c.id, c.name, c.service, c.priority, c.appointment_date, c.notes])
    print(f"Archivo generado: {nombre_archivo}")
