import random

class Profesor:
    def __init__(self,nombre,nota_minima,nota_maxima):
        validar_notas = {
            "min" : (0.0, 4.0),
            "max" : (6.0, 10.0)
        }
        def validar_nota_minima(nota_minima):
            min = validar_notas["min"][0]
            max = validar_notas["min"][1]

            if nota_minima < min:
                raise Exception(f'La nota mínima debe ser superior a {min}')
            if nota_minima >= max:
                raise Exception(f'La nota mínima debe ser inferior a {max}')

            return nota_minima
   
        def validar_nota_maxima(nota_maxima):
            min = validar_notas["max"][0]
            max = validar_notas["max"][1]

            if nota_maxima < min:
                raise Exception(f'La nota máxima debe ser superior a {min}')
            if nota_maxima > max:
                raise Exception(f'La nota máxima debe ser inferior a {max}')
            return nota_maxima

        self.nombre = nombre
        self.nota_minima = validar_nota_minima(nota_minima)
        self.nota_maxima = validar_nota_maxima(nota_maxima)

    def __str__(self) -> str:
        return f"{self.nombre} [{self.nota_minima}/{self.nota_maxima}]"

    def generar_nota(self) -> float:
        return random.uniform(self.nota_minima, self.nota_maxima)
