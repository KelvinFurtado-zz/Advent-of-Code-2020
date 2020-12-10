inputfile = open('inputDay02.txt', 'r')
inputlist = [i.split() for i in inputfile.readlines()]

def createrangelist(data):
    rangelst = [i[0] for i in data]
    rangelst = [i.split('-') for i in rangelst]
    rangeaux = []
    for i in rangelst:
        rangeaux = rangeaux + [[int(j) for j in i]]
    rangelst = [tuple(i) for i in rangeaux]
    return rangelst


def createletterlist(data):
    letterslist = [i[1] for i in data]
    letterslist = [i.strip(':') for i in letterslist]
    return letterslist


def createpasswordlist(data):
    return [i[2] for i in data]

# Part 1 counter
def counter(rangelist, letters, passwords):
    valid_passwords = 0
    for i in range(len(rangelist)):
        if passwords[i].count(letters[i]) in range(rangelist[i][0], rangelist[i][1] + 1):
            valid_passwords += 1
    return valid_passwords


# Part 2 counter
def newcounter(rangelist, letters, passwords):
    new_valid_passwords = 0
    for i in range(len(rangelist)):
        if bool(letters[i] == passwords[i][rangelist[i][0] - 1]) ^ bool(letters[i] == passwords[i][rangelist[i][1] - 1]):
            new_valid_passwords += 1
    return new_valid_passwords

rangelist = createrangelist(inputlist)
letters = createletterlist(inputlist)
passwords = createpasswordlist(inputlist)

print("Part 1:",counter(rangelist,letters,passwords))
print("Part 2:",newcounter(rangelist,letters,passwords))

inputfile.close()