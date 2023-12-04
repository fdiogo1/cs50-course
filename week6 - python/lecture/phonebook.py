import sys

people = {
    "Carter": "123456",
    "David": "7892222"
}

name = input("Name: ")
if name in people:
    number = people[name]
    print(f"Number: {number}")
    sys.exit(0)

print("Not found.")
sys.exit(1)
