from generate_names_emails import  generate_names_emails
from user import User

class Alumno(User):
    def __init__(self, name = None, turno = "A", email = None):
        super().__init__(name, email)
        self.turno = turno
        self.nota = 0

    def setNota(self,nota):
        self.nota = nota
      
    def __str__(self):
        buffer = []
        buffer.append(f"Alumno:{self.name} ") 
        buffer.append(f"Turno: {self.turno} ")
        buffer.append(f"Nota:{round(self.nota, 2)}")

        return "".join(buffer)

    def convocarExamen(self,turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.email}")        
            print(f" Estimado/a {self.name}, su nota del examen es - apto/a, convocado/a.")
            print(f"Nota:{round(self.nota, 2)}")

if __name__ == "__main__":
    alumno1 = Alumno()
    print (alumno1)
