s = input("Do you agree? ")

if s.lower() == "y":
    print("Agreed.")
elif s.lower() == "n":
    print("Not agreed.")
else:
    print("Try again")

# Another way:
if s == "Y" or s == "y":
    print("Agreed.")
elif s == "N" or s == "n":
    print("Not agreed.")
else:
    print("Try again")

# Another way
s = s.lower()
if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")
else:
    print("Try again.")
