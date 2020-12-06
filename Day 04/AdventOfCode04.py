'''
Part 1: Check how many passports are valid

1- Separate each passport.
2- To facilitate visualization, I ordered the passport parameters.
3- To check the passport, I first checked the number of fields in each passport
(less than 6 = invalid,7 is only valid if the "cid" field is missing and 8 = valid)

Part 2: Check if the information in each field is in the correct format, following the rules:
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.

Using regex for some fields, I checked all fields with the exception of the "cid" which is completely optional.
'''
import re
inputfile = open('inputDay04.txt', 'r')
passports_data = inputfile.read()
passports = passports_data.split("\n\n")

passports = [re.split(" |\n", i) for i in passports]

def sort_passport_info(passports):
    sorted_info = []
    for i in passports:
        sorted_info.append(sorted(i))
    return sorted_info

def passport_checker(passport):
    if len(passport) <= 6:
        return False
    if len(passport) == 7:
        check_cid = ["cid:" not in i for i in passport]
        return True if all(check_cid) else False
    if len(passport) == 8:
        return True

def counter_valid_passports(passports):
    counter = 0
    for i in passports:
        counter += passport_checker(i)
    return counter

def rulesverifier(passport):
    for i in passport:
        if "byr:" in i:
            numBYR = int(i[i.index(":")+1:])
            #print(numBYR)
            if numBYR not in range(1920, 2003):
             #   print("numBYR fora do range 1920 2003")
                return False
        if "ecl:" in i:
            ecl = i[i.index(":")+1:]
            #print(ecl)
            if not re.fullmatch("amb|blu|brn|gry|grn|hzl|oth", ecl):
             #   print("ecl não é amb blu brn gry grn hzl oth")
                return False
        if "eyr:" in i:
            numEYR = int(i[i.index(":")+1:])
            #print(numEYR)
            if numEYR not in range(2020,2031):
             #   print("numEYR fora do range 2020 2031")
                return False
        if "hcl:" in i:
            hcl = i[i.index(":")+1:]
            #print(hcl)
            if not re.fullmatch("^#([0-9]|[a-f]){6}", hcl):
                #print("hcl diferente do padrão")
                return False
        if "hgt:" in i:
            unit = i[-2:]
            numHGT = int(i[i.index(":")+1:-2])
            #print(numHGT, unit)
            if unit != "cm" and unit != "in":
                return False
            else:
                if unit == "cm":
                    if numHGT not in range(150,194):
                        #print("numHGT fora do range 150 194")
                        return False
                if unit == "in":
                    if numHGT not in range(59,77):
                        #print("numHGT fora do range 59 77")
                        return False
        if "iyr:" in i:
            numIYR = int(i[i.index(":")+1:])
            #print(numIYR)
            if numIYR not in range(2010,2021):
                #print("numIYR fora do range 2010 2021")
                return False
        if "pid:" in i:
            numPID = i[i.index(":")+1:]
            #print(numPID)
            if not re.fullmatch("[0-9]{9}", numPID):
                #print("numPID fora do padrão")
                return False
    return True

def new_counter_valid_passports(passports):
    new_counter = 0
    for i in passports:
        if passport_checker(i):
                new_counter += rulesverifier(i)
    return new_counter

passports = sort_passport_info(passports)
print("Part 1:",counter_valid_passports(passports))
print("Part 2:", new_counter_valid_passports(passports))

inputfile.close()