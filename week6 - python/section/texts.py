text = "In the great green room"
words = text.split()

# Round 1
print("Round 1")
for word in words:
    print(word)

# Round 2
print("Round 2")
for word in words:
    for c in word:
        print(c)

# Round 3
print("Round 3")
for word in words:
    if "g" in word:
        print(word)

# Round 4
print("Round 4")
for word in words[2:]:
    print(word)

# Round 5
print("Round 5")
for _ in words: # _ means that it doesn't matter.
    print("Goodnight Moon")
