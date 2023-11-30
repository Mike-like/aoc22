# part 1
sum = 0
for l in open("e4.txt"):
    l = l[:-1]
    r1 = range(int(l.split(",")[0].split("-")[0]), int(l.split(",")[0].split("-")[1])+1)
    r2 = range(int(l.split(",")[1].split("-")[0]), int(l.split(",")[1].split("-")[1])+1)
    if (r1[0] in r2 and r1[-1] in r2) or (r2[0] in r1 and r2[-1] in r1):
        sum += 1
print(sum)