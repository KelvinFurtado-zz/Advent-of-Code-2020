'''
Part 1: From a list containing in each line a range, a character and a string,
check how many strings are valid.
For the string to be valid, the number of occurrences of the character must be in the range.

First of all, you need to fit the data.
The "create range list" returns a list of tuples containing the range in int type numbers.
The "create letter list" returns a list with just the characters to be searched for each line.
The "create password list" returns a list with all the passwords.

the function checks if the number of occurrences of the character is within the range for each password.
If so, it increments a valid password counter.


Part 2: With the same list, check how many strings are valid according to the new policy.
The numbers are now the exact positions of the character in the password.
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant.

To check if the character is exactly in one of the positions, I used the bitwise operation (XOR)
'''

inputlist = [i.split() for i in open('inputDay02.txt', 'r').readlines()]

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
