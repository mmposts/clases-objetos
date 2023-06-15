import requests

def get_json_from(uri):
    r = requests.get(uri)

    return r.json()
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

def generate_name_email(results = 1):  
    
    uri = f'https://randomuser.me/api/?results={results}'
    r = requests.get(uri)
    randomuser = r.json()
    users = randomuser["results"]

    my_users_data = []
    if r.status_code == 200:
        r = r.json()
        for user in users:
            my_users_data.append({
                "name": f'{user["name"]["first"]} {user["name"]["last"]}',
                "email": user["email"]
            })

    return my_users_data

def __set__(self):
    buffer = []
    buffer.append(f"Name:{self.name.ljust(10)}",end =" - ") 
    buffer.append(f"Email: {self.email}",end = " -")

    return " ".buffer
        
def main():
    my_users_data = generate_name_email()
    for my_user in my_users_data:
        print(f"NAME: {my_user['name']}")
        print(f"EMAIL: {my_user['email']}")
        print()

if __name__ == "__main__":
   main()
    








# !/usr/bin/env python
# -*- coding: utf-8 -*-

#  polimorfismo.py
 
#  Copyright 2020 <<Pyro>>

# class testclass():                             #Clase de ejemplo
#     def over(self, a):                     #Creamos el método
#         if type(a) == int:             #Condicional para comprobar
#             print ("A es entero")  #el tipo de dato
#         elif type(a) == str:
#             print ("A es texto, ingresaste texto! no seas mamón!")

# Test = testclass()                              #Instancia

# a = (input("Ingresa un valor entero"))          #Pedimos un valor al user
# Test.over(a)                                    #Llamamos el método con el
#                                                 #valor que ingreso el usuario
