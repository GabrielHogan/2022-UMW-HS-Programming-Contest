key = map(int, input().split())
ciphertext = map(int, input().split())

plaintext = ''

for i, char in enumerate(ciphertext):
    plaintext += chr(char ^ key[i % len(key)])

print(plaintext)
