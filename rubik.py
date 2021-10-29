import random

i = 1
while i <=20:
    x =  random.randint(1,24)
    if x == 1:
        a = "R"
    elif x == 2:
        a = "R'"
    elif x == 3:
        a = "R2"
    elif x == 4:
        a = "R2'"
    elif x == 5:
        a = "F"
    elif x == 6:
        a = "F'"
    elif x == 7:
        a = "F2"
    elif x == 8:
        a = "F2'"
    elif x == 9:
        a = "U"
    elif x == 10:
        a = "U'"
    elif x == 11:
        a = "U2"
    elif x == 12:
        a = "U2'"
    elif x == 13:
        a = "B"
    elif x == 14:
        a = "B'"
    elif x == 15:
        a = "B2"
    elif x == 16:
        a = "B2'"
    elif x == 17:
        a = "L"
    elif x == 18:
        a = "L'"
    elif x == 19:
        a = "L2"
    elif x == 20:
        a = "L2'"
    elif x == 21:
        a = "D"
    elif x == 22:
        a = "D'"
    elif x == 23:
        a = "D2"
    elif x == 24:
        a = "D2'"
    print(a)
    i +=1


#R R' R2 R2' F F' F2 F2' U U' U2 U2' B B' B2 B2' L L' L2 L2' D D' D2 D2'
 