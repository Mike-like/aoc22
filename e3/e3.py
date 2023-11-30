#par1
sum = 0
for l in open("e3.txt").readlines():
    x = list(set(l[0:int(len(l)/2)]).intersection(set(l[int(len(l)/2):])))
    sum += ord(x[0])-96 if ord(x[0])-96 > 0 else ord(x[0])-38
print(sum)

#part2
sum = 0
f = open("e3.txt").readlines()
x = set(f[0])
f.pop(0)
for i, l in enumerate(f, 1):
    l = l[:-1]
    if i % 3 == 0:
        x = list(x)
        sum += ord(x[0]) - 96 if ord(x[0]) - 96 > 0 else ord(x[0]) - 38
        x = set(l)
    x = set(l).intersection(x)
x = list(x)
sum += ord(x[0]) - 96 if ord(x[0]) - 96 > 0 else ord(x[0]) - 38
print(sum)