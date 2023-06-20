from generate_names_emails import generate_names_emails


class User:
    def __init__(self, name=None, email=None):
        if name is None or email is None:
            user = generate_names_emails()[0]
            name = user["name"]
            email = user["email"]
        self.name = name if name is not None else user["name"]
        self.email = email if email is not None else user["email"]

        # print(f"Esto es el nombre de un usuario, {self}")

    def __str__(self):
        return f"Name:{self.name}_- Email: {self.email}"


# class Alumnos(User):
#     def __init__(self, name = None, nota = None, turno = " ", email = None):
#          super().__init__(name, email)
#          self.nota = nota
#          self.turno = turno
#     def __str__(self):
#         return User.__str__(self) + "(nota)" + "(turno)"
if __name__ == "__main__":
    user = User()

    print(user)
