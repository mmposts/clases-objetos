import random
from clases_de_alumnos import Alumno
from aula import Aula

turnos =["A", "B", "C"]              
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

