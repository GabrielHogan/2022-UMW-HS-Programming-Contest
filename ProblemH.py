galleons = int(input())
sickles = int(input())
knuts = int(input())

# galleons to knuts
galleons = galleons*493
knuts = knuts + galleons
galleons = 0

# sickles to knuts
sickles = sickles*29
knuts = knuts + sickles
sickles = 0

galleons = knuts//493
knuts = knuts % 493
print(galleons)

sickles = knuts//29
knuts = knuts % 29
print(sickles)

print(knuts)
