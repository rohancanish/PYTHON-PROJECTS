string = input("Enter a string: ")
d = {}
words = string.lower().split()

for w in words:
    if w not in d:
        d[w] = 1
    else:
        d[w] += 1

print(d)
for word, count in d.items():
    print(f"'{word}' occurs {count} times")
