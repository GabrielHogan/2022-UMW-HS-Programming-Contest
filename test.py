num = int(input())
imp = input().split()
x = 0
y = 0
v = 1
sum = 0
tot = num * num
tc = 0

# print(imp)
for y in range(len(imp)):
    for x in range(len(imp)):
        if(v % 2 == 0):
            sum = sum + int(imp[int(x)])
        else:
            sum = sum - int(imp[int(x)])

        v = v + 1
        tc = tc + 1
        if(tc == tot):
            if(v % 2 == 0):
                sum = sum + int(imp[int(x)])
            else:
                sum = sum - int(imp[int(x)])
            if(sum == int(imp[int(x)])):
                print("Prize!")
            else:
                print("No prize!")
    imp = input().split()

   # x = 0
#  y = y + 1
# print(imp[num-1])
#y = y + 1
""""if(v%2 == 0):
  sum = sum + int(imp[num-1])
else:
  sum = sum - int(imp[num-1])
  
if(sum == int(imp[num-1])):
  print("Prize!")
else:
  print("No prize!")"""
