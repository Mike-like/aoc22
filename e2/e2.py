#part 1
sum = 0
for l in open("e2.txt"):
    sum += ord(l[2])-87
    player_int = ord(l[2])-23
    cpu_int = ord(l[0])
    if player_int == cpu_int:
        sum += 3
    elif player_int - cpu_int in (-2, 1):
        sum += 6
print(sum)

# part 2
sum = 0
for l in open("e2.txt"):
    options = (1, 1, -2)
    options_lose = (2, -1, -1)
    player_move = 0
    if l[2] == 'Z':
        sum += 6
        player_move = ord(l[0]) + options[ord(l[0])-65] - 64
    elif l[2] == 'Y':
        sum += 3
        player_move = ord(l[0]) - 64
    else:
        player_move = ord(l[0]) + options_lose[ord(l[0])-65] - 64
    sum += player_move

print(sum)