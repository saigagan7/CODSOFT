import random
import string

def password_generator(username, length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = username[0] + ''.join(random.choice(password_characters) for i in range(length-1))
    return password

username = input("Enter user name: ")
password_length = int(input("Enter password length: "))

generated_password = password_generator(username, password_length)
print("Generated password: ", generated_password)