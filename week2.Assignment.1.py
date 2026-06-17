import random
import string

num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the number of characters for each password: "))

characters = string.ascii_letters + string.digits + string.punctuation

print("\ngenerated passwords: ")
for i in range(num_passwords):
    password = ''.join(random.choice(characters) for _ in range(password_length))
    print(f"password{i+1}: {password}")


import os

current_directory =os.getcwd()
print("current working directory: ")


import csv
import os
filename = input("Enter the name of the csv file (e.g; data.csv): ")


if os.path. exists(filename):
    print("file existing")
else:
    print("file does not exist. creating file")
    with open(filename, "w", newline = "") as file:
        writer = csv.writer(file)
        
        writer.writerow(["name", "age", "gender"])
        name = input("enter your name: ")
        age = input("enter your age: ")
        gender = input("enter your gender: ")
    with open(filename, "a", newline="")as file:
        writer = csv.writer(file)
        writer.writerow([name, age, gender])
    print("information successfully written to the csv file")

