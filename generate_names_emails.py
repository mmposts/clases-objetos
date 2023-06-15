import requests

def get_json_from(uri):
    r = requests.get(uri)

    return r.json()

def generate_names_emails(results = 1):  
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

if __name__ == "__main__":
    my_users_data = generate_names_emails(10)
    for my_user in my_users_data:
        print(f"NAME: {my_user['name']}")
        print(f"EMAIL: {my_user['email']}")
        print()
    