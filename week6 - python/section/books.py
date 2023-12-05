books = []

# Add three books to your shelf

for i in range(3):
    book = dict()
    book["title"] = input("Title: ").strip().capitalize() # remove the blank spaces, and capitalize the first letter
    book["author"] = input("Author: ").strip()
    books.append(book)

for book in books:
    print("Title: "+ book["title"])
