line = input()

line_length = len(line)

if line_length < 6:
    print("Invalid")
    exit()

p1, p2 = 0, 0
has_digital = False
has_alpha = False

while p1 < line_length:
    if line[p1].isdigit():
        has_digital = True
    elif line[p1].isalpha():
        has_alpha = True
    p2 = p1 + 1

    if p2 == line_length:
        break

    while line[p1] == line[p2]:
        if p2 - p1 >= 2:
            print("Invalid")
            exit()
        p2 += 1

    p1 = p2

if not has_digital or not has_digital:
    print("Invalid")
else:
    print("Valid")
