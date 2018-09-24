# CS2303
# NAME: Stephanie Callejas
# Assigment: Lab 1 Option C
# Instructor: Diego Aguirre
# T.A: Manoj Saha
# Date: September 17, 2018
# Purpose: Find the real password that is hashed in the users file document


import hashlib
from itertools import product

user_name = {}
comList = "0123456789"
list_of_passwords = []


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))

    hex_dig = hash_object.hexdigest()

    return hex_dig


def processFileLine(record):
    values = record.split(',')
    user_name[values[0]] = values


def generatePassword(lowerLimit, upperLimit):
    list_of_passwords = product(comList, repeat=lowerLimit)
    lowerLimit += 1
    for i in list(list_of_passwords):
        gen_pass = ''.join(i)
        print("Generated Password: " + gen_pass)
        checkForPassword(gen_pass)
        if lowerLimit <= upperLimit:
            generatePassword(lowerLimit, upperLimit)


def checkForPassword(gen_pass):
    for key, value in user_name.items():
        if value[2] == hash_with_sha256(gen_pass.join(value[1])):
            print("Password Matches user: " + key)
        else:
            print("has no password")


def main():
    with open('password_file.txt') as openfileobject:
        for record in openfileobject:
            processFileLine(record)

    generatePassword(3, 6)


main()