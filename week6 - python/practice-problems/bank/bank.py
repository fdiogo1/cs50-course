greet = input("Greeting: ").lower().split()

check = greet[0]

if "h" in check:
    if "hello" in check:
        print("$0")
    elif check[0] == "h":
        print("$20")
    else:
        print("$100")
else:
    print("$100")
