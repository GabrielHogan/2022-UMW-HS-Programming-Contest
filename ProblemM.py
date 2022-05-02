num_inputs = int(input())

participants = []

for _ in range(num_inputs):
    [name, age] = input().split(': ')
    participants.append((name, int(age)))

team1 = []
team2 = []

for (name, age) in participants:
    if age % 2 == 0:
        team2.append((name, age))
    else:
        team1.append((name, age))

team1 = sorted(team1, key=lambda x: x[1])
team2 = sorted(team2, key=lambda x: x[1], reverse=True)

print('Team 1')
[print(f'{name}: {age}') for (name, age) in team1]

print()

print('Team 2')
[print(f'{name}: {age}') for (name, age) in team2]
