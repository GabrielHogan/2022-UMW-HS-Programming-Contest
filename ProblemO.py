class Player:
    def __init__(self, name, bravery, dedication, intellegence, ambition):
        self.name = name
        total = bravery + dedication + intellegence + ambition
        self.bravery = bravery / total
        self.dedication = dedication / total
        self.intellegence = intellegence / total
        self.ambition = ambition / total


num_players = int(input())

players = []
for _ in range(num_players):
    name, bravery, dedication, intellegence, ambition = input().split()
    players.append(Player(name, int(bravery), int(
        dedication), int(intellegence), int(ambition)))

# sort players alphabetically by name
players = sorted(players, key=lambda x: x.name)

# Create teams for captains: Jennifer, Tray, Coco, and Calins
teamJennifer = []
teamTray = []
teamCoco = []
teamCalins = []

# Round robin choose teams by preference in traits if equal then alphabetical. Jennifer prefers bravery, Tray prefers dedication, Coco prefers intelligence, and Calins prefers ambition.

preferences = ['bravery', 'dedication', 'intellegence', 'ambition']

for i in range(len(players)):
    trait = preferences[i % 4]
    # get player with highest trait score and assign to team
    top_player = max(players, key=lambda x: getattr(x, trait))

    players.remove(top_player)

    if trait == 'bravery':
        teamJennifer.append(top_player)
    elif trait == 'dedication':
        teamTray.append(top_player)
    elif trait == 'intellegence':
        teamCoco.append(top_player)
    else:
        teamCalins.append(top_player)


print('Jennifer:')
teamJennifer = sorted(teamJennifer, key=lambda x: x.name)
[print(f'{player.name}') for player in teamJennifer]

print()

print('Tray:')
teamTray = sorted(teamTray, key=lambda x: x.name)
[print(f'{player.name}') for player in teamTray]

print()

print('Coco:')
teamCoco = sorted(teamCoco, key=lambda x: x.name)
[print(f'{player.name}') for player in teamCoco]

print()

print('Calins:')
teamCalins = sorted(teamCalins, key=lambda x: x.name)
[print(f'{player.name}') for player in teamCalins]
