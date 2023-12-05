import csv, sys

titles = []

with open("books.csv") as file:
    text = csv.DictReader(file)
    for row in text:
        titles.append(row['title'])

    name = input("Type the title you are looking for: ")

    if name in titles:
        print("Yes")
        sys.exit(0)
    else:
        print("Not found.")
        sys.exit(1)

