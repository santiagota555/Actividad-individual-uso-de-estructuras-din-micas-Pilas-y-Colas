from logic import ingresar_clientes
from service import mostrar_lista_fecha, mostrar_lista_urgencia, mostrar_lista_total

if __name__ == "__main__":
    pacientes = []
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Ingresar pacientes")
        print("2. Mostrar lista en orden de fecha")
        print("3. Mostrar lista en orden de urgencia")
        print("4. Mostrar lista total (Urgentes primero, por hora)")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            pacientes.extend(ingresar_clientes())
        elif opcion == "2":
            mostrar_lista_fecha(pacientes) if pacientes else print("No hay pacientes.")
        elif opcion == "3":
            mostrar_lista_urgencia(pacientes) if pacientes else print("No hay pacientes registrados con caracter urgente.")
        elif opcion == "4":
            mostrar_lista_total(pacientes) if pacientes else print("No hay pacientes.")
        elif opcion == "5":
            print(" Saliendo...    \n(GRACIAS POR PROBAR EL PROGRAMA)\n(ELABORADO POR: Santiago Toro Amariles)\n(UNIVERSIDAD DE MANIZALES)\n(Actividad individual: uso de estructuras dinámicas Pilas y Colas)")
            break
        else:
            print("Opción inválida.")
