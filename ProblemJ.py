num_pirates = int(input())

pirates = []

for _ in range(num_pirates):
    pirates.append(input().split())

for pirate in pirates:
    name = pirate[0]
    min_born, max_born, min_died, max_died = map(int, pirate[1:])

    print(f'{name} lived to between the ages of {min_died - max_born} to {max_died - min_born}.')
