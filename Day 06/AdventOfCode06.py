inputfile = open('inputDay06.txt', 'r')
data = inputfile.read()
groups = data.split("\n\n")
groups = [i.split("\n") for i in groups]

#PART 1
def counter(group):
    charlist = []
    for i in group:
        for j in i:
            if j not in charlist:
                charlist += j
    return len(charlist)

def counters_sum(groups):
    sum = 0
    for i in groups:
        sum += counter(i)
    return sum


#PART 2
def new_counter(group):
    charlist = []
    in_all = []
    letters = []
    for i in group:
        for j in i:
            if j not in charlist:
                charlist += j

    for j in charlist:
        in_all = [j in i for i in group]
        if all(in_all):
            letters += j
    return len(letters)

def new_counters_sum(groups):
    sum = 0
    for i in groups:
        sum += new_counter(i)
    return sum


print("Part 1:", counters_sum(groups))
print("Part 2:", new_counters_sum(groups))

inputfile.close()