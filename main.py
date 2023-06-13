# import random
from clases_de_alumnos import Alumno
from aula import Aula
from profesor import Profesor

turnos =["A", "B", "C"] 
profe = Profesor
             
alumnos = [    
    Alumno( "Manolo", turnos[1], "manolo43@.com" ),
    Alumno( "Paco", turnos[0], "abcpaco@.com"),
    Alumno( "Flor", turnos[0], "florcillamala@.com"),
    Alumno( "Jose", turnos[1], "joselito123@.com"),

]
aula = Aula()
aula.add(Alumno("Blue", turnos[0], "blue3@.com" ))
aula.add(Alumno ("Safari", turnos[0], "safari@.com"))
aula.add(Alumno("COCODRILO", turnos[0], "cocoanimal@.com"))
aula.add(Alumno("Josefa", turnos[0], "josefinia3@.com"))

aula.lista()
aula.convocarExamen("A")

profes = [
    Profesor( "Francisco Perez", 4, 10),
    Profesor("Marta Sanches", 4, 9),
    Profesor("Enrique Bolaños", 5, 10),
    Profesor("Franchesca Rivas", 5, 10),
    Profesor("Miguel Santos", 2, 7),
]