import math as m

InitKnuts = int(input())
Weeks = int(input())
CurrentKnuts = InitKnuts

for i in range(Weeks):
    tempCurrent = CurrentKnuts
    CurrentKnuts -= m.ceil(tempCurrent/20)
    CurrentKnuts += m.floor(tempCurrent/16)
    if CurrentKnuts >= 10:
        CurrentKnuts -= 3

if (CurrentKnuts > 0):
    print("After " + str(Weeks) + " weeks there are " +
          str(CurrentKnuts) + " knuts.")
else:
    print("After " + str(Weeks) + " weeks there are no more knuts!")
