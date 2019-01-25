l = input().split(" ")
valid_oper = ("U", "D", "L", "R")
height = int(l[0]) - 1
width = int(l[1]) - 1

pos = {"x": 0, "y": 0}
for _ in range(0, int(l[2])):
    oper = input()
    if oper not in valid_oper:
        print("invalid")
        exit()
    if oper == "U":
        if pos["y"] == height:
            print("invalid")
            exit()
        else:
            pos["y"] += 1
    elif oper == "D":
        if pos["y"] == 0:
            print("invalid")
            exit()
        else:
            pos["y"] -= 1
    elif oper == "L":
        if pos["x"] == 0:
            print("invalid")
            exit()
        else:
            pos["x"] -= 1
    elif oper == "R":
        if pos["x"] == width:
            print("invalid")
            exit()
        else:
            pos["x"] += 1
    print(pos)
print("valid")
