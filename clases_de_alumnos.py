class Alumno:
    def __init__(self,nombre, turno, correo):
        self.nombre = nombre
        self.turno = turno
        self.correo = correo
        self.nota = 0

    def __set__(self):
        buffer = []
        buffer.append(f"Alumno:{self.nombre.ljust(8)}",end =" - ") 
        buffer.append(f"Turno: {self.turno}",end = " -")
        buffer.append(f"Nota:{self.nota}")

        return "".buffer

    def convocarExamen(self,turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")        
            print(f" Estimado/a {self.nombre}, su nota del examen es - apto/a, convocado/a.")
            print(f"Nota:{self.nota}")

    def setNota(self,nota):
        self.nota = nota
