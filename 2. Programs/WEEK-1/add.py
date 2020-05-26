inputList = list(map(int, input().strip().split()))[:3]

x = inputList[0]
y = inputList[0] - inputList[1] 
z = inputList[2]

i1 = 0
i2 = 0

flag1 = 0
flag2 = 0

a1 = x

if z == 0:
    print("0")

elif z == a1:
    print("1")

else:
    if y!=0:
        if z % y == 0:
            a = z // y+1

            if a > 0:
                i1 = 2*(a-1)
                flag1 = 1

        if (z-a1) % y ==0:
            b = (z-a1) // y+1

            if b > 0:
                i2 = 2*(b-1)+1

                flag2 = 1

        if flag1 == 0:
            i1 = 0

        if flag2 == 0:
            i2 = 0

        if i1 > i2 and i2 == 0:
            print(i1)

        elif i1 < i2 and i2!=0:
            print(i2)

        elif i1==0 and i2 ==0:
            print("-1")

        elif i2>i1 and i1 == 0:
            print(i1)

        elif i2<i1 and i1 !=0:
            print(i2)

    else:
        print("-1")












