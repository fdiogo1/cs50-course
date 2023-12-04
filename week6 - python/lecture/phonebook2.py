import csv

with open("phonebook.csv", "a") as file: # so we don't need to worry about closing the file
    name = input("Name: ")
    number = input("Number: ")

    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})
