l = input().split(" ")

f = "{:0>" + l[0] + "d}"
for i in range(int(l[1]), int(l[2]) + 1):
    print(f.format(i))
