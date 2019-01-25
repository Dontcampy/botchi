count = int(input())


def static(team):
    t = 0
    W = 0
    D = 0
    L = 0
    for string in team:
        if string == "W":
            t += 2
            W += 1
        elif string == "D":
            t += 1
            D += 1
        elif string == "L":
            L += 1
    return t, W, D, L


winner = [-1, -1, -1, -1, -1]  # winner[0] for team cursor, winner[1] for winner score
for i in range(0, count):
    team = input()

    static_data = static(team)
    if static_data[0] > winner[1]:
        winner[0] = i
        winner[1] = static_data[0]
        winner[2] = static_data[1]
        winner[3] = static_data[2]
        winner[4] = static_data[3]

winner[0] += 1
print(" ".join([str(x) for x in winner]))
