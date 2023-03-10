import hashlib
import json

def password_checker(password):

    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False

    if not any(char in "!@#$%^&*" for char in password):
        return False

    return True

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()

def add_password(passwords):
    password = input("Choisissez un nouveau mot de passe : ")

    while not password_checker(password):
        print("Le mot de passe ne respecte pas les exigences de sécurité.")
        password = input("Choisissez un nouveau mot de passe : ")

    passwords[password] = hash_password(password)
    print("Mot de passe ajouté avec succès.")
    return passwords

def display_passwords(passwords):
    print("Liste des mots de passe :")
    for password, hashed_password in passwords.items():
        print(f"- {password}: {hashed_password}")

def save_passwords(passwords):
    with open("passwords.json", "w") as f:
        json.dump(passwords, f)
    print("Mots de passe enregistrés.")

try:
    with open("passwords.json", "r") as f:
        passwords = json.load(f)
except FileNotFoundError:
    passwords = {}

while True:
    print("1. Ajouter un mot de passe")
    print("2. Afficher les mots de passe")
    print("3. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        passwords = add_password(passwords)
    elif choice == "2":
        display_passwords(passwords)
    elif choice == "3":
        break

save_passwords(passwords)
