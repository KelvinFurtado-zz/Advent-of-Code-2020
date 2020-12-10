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