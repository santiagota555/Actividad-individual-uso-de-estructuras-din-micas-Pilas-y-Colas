from datetime import datetime

class Client:
    def __init__(self, id, name, service, priority, appointment_date, notes=""):
        self.id = id
        self.name = name
        self.service = service
        self.priority = priority
        self.appointment_date = appointment_date
        self.notes = notes

SERVICIOS = ["Extracción", "Limpieza", "Sellado", "Ortodoncia"]
PRIORIDADES = ["Urgente", "Normal"]
