if __name__ == '__main__':
    snacks = [0]
    #part 1
    # top = 1
    #part 2
    top = 3
    for l in open("e1.txt"):
        if l == "\n":
            snacks.append(0)
        else:
            snacks[-1] += int(l)
    print(sum(sorted(snacks)[top*-1:]))
