from logic import exportar_csv

def mostrar_lista_fecha(clientes):
    lista = sorted(clientes, key=lambda c: c.appointment_date)
    print("\nPacientes ordenados por fecha:")
    for c in lista:
        print(f"ID:{c.id} | Nombre:{c.name} | Servicio:{c.service} | "
              f"Prioridad:{c.priority} | Fecha:{c.appointment_date} | Notas:{c.notes}")
    exportar_csv("lista_por_fecha.csv", lista)

def mostrar_lista_urgencia(clientes):
    lista = sorted(clientes, key=lambda c: (0 if c.priority == "Urgente" else 1, c.appointment_date))
    print("\nPacientes ordenados por urgencia:")
    for c in lista:
        print(f"ID:{c.id} | Nombre:{c.name} | Servicio:{c.service} | "
              f"Prioridad:{c.priority} | Fecha:{c.appointment_date} | Notas:{c.notes}")
    exportar_csv("lista_por_urgencia.csv", lista)
def mostrar_lista_total(clientes):
    lista = sorted(clientes, key=lambda c: (0 if c.priority == "Urgente" else 1, c.appointment_date))
    print("\nLista total (Urgentes primero, luego Normales, por hora):")
    for c in lista:
        print(f"ID:{c.id} | Nombre:{c.name} | Servicio:{c.service} | "
              f"Prioridad:{c.priority} | Fecha:{c.appointment_date} | Notas:{c.notes}")
    exportar_csv("lista_total.csv", lista)
