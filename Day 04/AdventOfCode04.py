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