import numpy as np
import classes


def parse(path):
    with open(path, 'r') as file:
        data = file.read()
    data = data.strip()

    constant_address_pointer = 15

    instructions = []
    variables = {}

    for line in data.split('\n'):
        fields = line.split(' ')
        if fields[0] == "var":
            name = fields[1]
            variable = classes.Variable(name, int(fields[2]), constant_address_pointer)
            variables[name] = variable
            constant_address_pointer -= 1
        else:
            mnemonic = fields[0]
            operands = fields[1:]
            for i, o in enumerate(operands):
                if o in variables.keys():
                    operands[i] = variables[o].address
            operands = [int(o) for o in operands]
            instruction_format = classes.format_map[mnemonic]
            instruction = instruction_format(mnemonic, operands)
            instructions.append(instruction)

    return instructions, variables.values()


def format_rom(rom: np.ndarray):
    out = "v2.0 raw"
    acc = -1
    count = 1
    n = 0
    flag = False
    for i in rom:
        if n % 8 == 0 and not flag:
            out += '\n'
            flag = True
        if i == acc:
            count += 1
        elif count > 1:
            n += 1
            flag = False
            out += f"{count}*{acc} "
            count = 1
        elif acc != -1:
            n += 1
            flag = False
            out += acc + ' '

        acc = i

    if count > 1:
        out += f"{count}*{acc} "
    else:
        out += acc

    return out


def write(path: str, s: str):
    with open(path, 'w') as file:
        file.write(s)
