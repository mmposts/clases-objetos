# from generate_names_emails import generate_names_emails
# from user import User


class DataUserGenerator:
    def __init__(self, cantidad_de_usuarios):
        self.next_user = 0
        self.users = []
        users = {
            "aula1": {"alumnos": 60, "profesores": 5},
            "aula2": {"alumnos": 30, "profesores": 4},
            "aula3": {"alumnos": 25, "profesores": 3},
            "aula4": {"alumnos": 33, "profesores": 4},
        }

    def generar_usuario(self):
        user = self.users[self.next_user]
        self.next_user += 1
        if self.next_user >= len(self.users):
            raise Exception("No hay usuarios disponibles")


user = DataUserGenerator()
print(user)
