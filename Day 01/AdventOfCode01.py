'''
Part 1: From a list of values, find two numbers that add up to 2020 and then multiply them together.

In the loop, if the number in that iteration is one of the two numbers,
what is missing for 2020 needs to be on the list too, so I look for the rest on the list.

Part 2: From a list of values, find three numbers that add up to 2020 and then multiply them together.

First of all, two variables without numeric value are created.
For the first loop, if the number of that iteration is one of the three values,
I look for two other values that add up to what is missing for 2020.
If the three values are in the list, the three are multiplied together.
'''
inputfile = open('inputDay01.txt', 'r')
values = [int(i) for i in inputfile.readlines()]
#PART1
def aoc01(numbers, value):
    for x in numbers:
        if value - x in numbers:
            return x * (value - x)

#PART2
def aoc02(numbers, value):
    num1, num2 = None, None
    for x in numbers:
        n = value - x
        for y in numbers:
            if n-y in numbers:
                num1 = y
                num2 = n-y
                if x + num1 + num2 == value:
                    return x * num1 * num2

print("Part1:",aoc01(values,2020))
print("Part2:",aoc02(values,2020))

inputfile.close()