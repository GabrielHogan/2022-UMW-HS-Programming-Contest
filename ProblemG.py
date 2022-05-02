amount = int(input())
total = 0

for a in range(amount):
    inp = int(input())
    total += inp*2


words = (total//2) + 1

print("You must examine " + str(words) + " words in the second file.")
