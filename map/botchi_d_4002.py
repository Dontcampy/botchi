count = int(input())

for _ in range(0, count):
    line = input()
    l = line.split(" ")
    if l[1] == "3":
        print(l[0])
