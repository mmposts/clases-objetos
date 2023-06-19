# import random
from alumno import Alumno
from aula import Aula
from profesor import Profesor

turnos =["A", "B", "C"] 
CANTIDAD =  {
    "profesor" : 8,
    "alumnos"  : 30,
    "aulas"    : 5
}

aulas = []
for i in range(CANTIDAD["aulas"]):
    aulas.append(Aula())

profesores = [
    # Profesor( "Francisco Perez", 0, 10),
    # Profesor("Marta Sanches", 0, 10),
    # Profesor("Enrique Bolaños", 0, 10),
    # Profesor("Franchesca Rivas", 0, 10),
    # Profesor("Miguel Santos", 0, 10),
]
for i in range(CANTIDAD["profesor"]):
    profesores.append(Profesor())
alumnos = []
for i in range(CANTIDAD["alumnos"]):
    alumnos.append(Alumno())

aulas[0].set_profesor(profesores[0])
aulas[1].set_profesor(profesores[1])
aulas[2].set_profesor(profesores[2])
aulas[4].set_profesor(profesores[0])

contador = 0
while contador < len(alumnos):
    aulas[contador % (len(aulas) - 1)].add(alumnos[contador])
    contador += 1

contador = 0
for aula in aulas:
    print("\n" * 1)
    print(f"AULA {contador} ----------------------------- ")
    contador += 1

    try:
        aula.puntuar()
    except Exception as e:
        print(e)

    aula.lista()

    try:
        aula.convocarExamen("A")
    except Exception as e:
        aula.lista()
        print(e)

print()