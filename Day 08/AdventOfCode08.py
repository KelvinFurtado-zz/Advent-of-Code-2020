import copy
inputfile = open('inputDay08.txt','r')
commands = inputfile.read().splitlines()
commands = [i.split() for i in commands]
commands = [[i[0],int(i[1])] for i in commands]

def execute_ops(commands):
    i = 0
    accumulator = 0
    was_visited = [False for i in commands]
    while (0 <= i < len(commands)) and (not was_visited[i]):
        if commands[i][0] == "nop":
            was_visited[i] = True
            i += 1
        elif commands[i][0] == "acc":
            accumulator += commands[i][1]
            was_visited[i] = True
            i += 1
        else:
            was_visited[i] = True
            i += commands[i][1]

    final = i == len(commands)
    return accumulator, final

def new_execution(commands):
    for i, command in enumerate(commands):
        operation, num = command
        if operation in ["nop", "jmp"]:
            commands_copy = copy.deepcopy(commands)
            commands_copy[i][0] = "nop" if operation == "jmp" else "jmp"
            new_accumulator, new_final = execute_ops(commands_copy)
            if new_final:
                return new_accumulator


accumulator, final = execute_ops(commands)

print("Part 1:",accumulator)
print("Part 2:", new_execution(commands))