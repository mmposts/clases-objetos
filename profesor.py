import random
from user import User

class Profesor(User):

    validar_notas = {
            "min" : (0.0, 4.0),
            "max" : (6.0, 10.0)
    }    

    def __init__(self):
        super().__init__()
    
        def validar_nota_minima(nota_minima):
            min =self. validar_notas["min"][0]
            max = self.validar_notas["min"][1]

            if nota_minima < min:
                raise Exception(f'La nota mínima debe ser superior a {min}')
            if nota_minima >= max:
                raise Exception(f'La nota mínima debe ser inferior a {max}')

            return nota_minima
   
        def validar_nota_maxima(nota_maxima):
            min = self.validar_notas["max"][0]
            max = self.validar_notas["max"][1]

            if nota_maxima < min:
                raise Exception(f'La nota máxima debe ser superior a {min}')
            if nota_maxima > max:
                raise Exception(f'La nota máxima debe ser inferior a {max}')
            return nota_maxima

        # self.name = name
        # self.nota_minima = validar_nota_minima(nota_minima)
        # self.nota_maxima = validar_nota_maxima(nota_maxima)
        min_min = self.validar_notas["min"][0]
        min_max = self.validar_notas["min"][1]
        max_min = self.validar_notas["max"][0]
        max_max = self.validar_notas["max"][1]

        self.nota_minima = round(random.uniform(min_min, min_max),2)
        self.nota_maxima = round(random.uniform(max_min,max_max), 2)

    def __str__(self) -> str:
        return f"{self.name} [{self.nota_minima}/{self.nota_maxima}]"

    def generar_nota(self) -> float:
        return random.uniform(self.nota_minima, self.nota_maxima)
   
profesor1 = Profesor()
print(profesor1)

    
