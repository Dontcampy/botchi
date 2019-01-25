count = int(input())

w_a, w_b = 0, 0


def func(a, b):
    global w_a, w_b
    if a == b:
        return
    if a == "g":
        if b == "c":
            w_a += 1
        else:
            w_b += 1
    elif a == "c":
        if b == "p":
            w_a += 1
        else:
            w_b += 1
    elif a == "p":
        if b == "g":
            w_a += 1
        else:
            w_b += 1


for _ in range(0, count):
    l = input().split(" ")
    func(l[0], l[1])
print(w_a)
print(w_b)
