from cs50 import get_int

scores = []
for i in range(3):
    score = get_int("Score: ")
    scores.append(score)
    # scores += [score] -> same thing

average = sum(scores) / len(scores)
print(f"Average: {average:.1f}")