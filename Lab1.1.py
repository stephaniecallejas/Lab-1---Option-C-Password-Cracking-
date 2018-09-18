#CS2303
#NAME: Stephanie Callejas
#Assigment: Lab 1 Option C
#Instructor: Diego Aguirre
#T.A: Manoj Saha
#Date: September 17, 2018
#Purpose: Find the real password that is hashed in the users file document


import hashlib
import itertools


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))

    hex_dig = hash_object.hexdigest()

    return hex_dig


def main():
    a = input("Minimum password length ");
    b = input("Maximum password length ");
    list = []

    #password generated of maximum length J
    for j in range(int(a), int(b) + 1):
        for i in itertools.product([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], repeat=int(j)):
            list.append(''.join(map(str, i)))
    print("Password generated")

    #reads the users file
    input_file = open("password_file.txt", "r")

    #reads the file then splits the name, salt and hashed value
    for line in input_file:
        name, salt, hashed_value = line.split(",");
        salt.replace(" ", " ");
        hashed_value.replace(" ", " ")
        print("Applying bruteforce for ", name)
    for password in list:
        password.replace(" ", " ");

    #concatenate s with a user's salt value and apply the hashlib.sha256 method to the resulting string.
        hex_dig = hash_with_sha256(salt + password);
    if (hex_dig == hashed_value):
        print(name + "has password: " + password)


main()