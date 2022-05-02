amount = int(input())
list = []

for a in range(amount):
    w = int(input())
    list.append(w)

list.sort()

words = list[0] + amount

print("You must examine " + str(words) + " words in the second file.")
