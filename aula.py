import random
from clases_de_alumnos import Alumno

class Aula:
    def __init__(self):
        self.alumnos = list()
        self.profesor = list()
        # print (f"Nueva aula de alumnos")

    def add(self,nuevoAlumno):
        self.alumnos.append(nuevoAlumno)

    def lista(self):
        print(f"Profesor: {self.profesor}")      
        for alumno in self.alumnos:
            # alumno.setNota(random.randint(3,10))
            alumno.describe()

    def convocarExamen(self,turno): 
        print(f"Profesor: {self.profesor}")      
        for alumno in self.alumnos:
            alumno.convocarExamen(turno)

    def puntuar_examen(self):
        for alumno in self.alumnos:
            alumno.setNota(self.profesor.generar_nota())
            alumno.describe()

    def setProfesor(self,profesor):
        self.profesor = profesor        
                
   
        










