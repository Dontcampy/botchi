line1 = input()
line2 = input()

success = 0
for n in line2.split(" "):
    if int(n) > 5:
        success += 1

print(success)
