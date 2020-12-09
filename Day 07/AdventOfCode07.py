def format_rule(rule):
    rule = rule[:-1]
    bag, content = rule.split(" bags contain ")
    content = content.split(", ")
    if "no other bags" in content:
        return bag, []
    content = [a[:a.index(" bag")] for a in content]
    return bag, format_content(content)

def format_content(content):
    container = []
    for i in content:
        contain, color = i[0], i[2:]
        container.append((int(contain),color))
    return container

def search_shiny_gold(bag, rules):
    if bag == "shiny gold":
        return True
    return any(search_shiny_gold(bag, rules) for _,bag in rules[bag])

def inside_shiny_gold(bag, rules):
    return 1 + sum(content * inside_shiny_gold(color, rules) for content,color in rules[bag])

inputfile = open('inputDay07.txt','r')
rules = [i.rstrip() for i in inputfile.readlines()]
rules = dict([format_rule(rule) for rule in rules])

print("Part 1:",sum(search_shiny_gold(i,rules) for i in rules if i != "shiny gold"))
print("Part 2:",inside_shiny_gold("shiny gold", rules) - 1)