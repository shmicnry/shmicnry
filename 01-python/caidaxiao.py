import random
i = 0
j = 0
while i<4:
    a = int(input("石头剪刀布："))
    b = random.randint(1,3)
    print(f'电脑的出拳是{b}')
    if ((a==1) and (b==2) or (a==2) and (b==3) or (a==3) and (b==1)):
        j += 1
        i += 1
        continue
    elif a == b:
        continue
    else:
        i += 1
        continue
if j == 3:
    print("you are win")
else:
    print("you are lose")