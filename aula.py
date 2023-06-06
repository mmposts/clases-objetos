import random
from clases_de_alumnos import Alumno

class Aula:
    def __init__(self):
        self.alumnos = list()
        print (f"Nueva aula de alumnos")

    def add(self,nuevoAlumno):
        self.alumnos.append(nuevoAlumno)

    def lista(self):
        for alumno in self.alumnos:
            alumno.setNota(random.randint(3,10))
            alumno.describe()

    def convocarExamen(self,turno):       
        for alumno in self.alumnos:
            alumno.convocarExamen(turno)
    
            
                











