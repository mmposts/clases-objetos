from generate_names_emails import  generate_names_emails

class Alumno:
    def __init__(self, nombre = None, turno = "A", correo = None):

        if nombre is None or correo is None:
            print("randomuser...")
            user = generate_names_emails()[0]
            nombre = user['name']
            correo = user['email']

        self.nombre = nombre
        self.turno = turno
        self.correo = correo
        self.nota = 0

    def __str__(self):
        buffer = []
        buffer.append(f"Alumno:{self.nombre.ljust(8)} ") 
        buffer.append(f"Turno: {self.turno} ")
        buffer.append(f"Nota:{self.nota}")

        return "".join(buffer)

    def convocarExamen(self,turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")        
            print(f" Estimado/a {self.nombre}, su nota del examen es - apto/a, convocado/a.")
            print(f"Nota:{self.nota}")

    def setNota(self,nota):
        self.nota = nota
