from abc import ABC, abstractmethod
from util import format_binary


class RamContent:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Instruction(RamContent):
    @abstractmethod
    def __init__(self, mnemonic):
        self.mnemonic = mnemonic
        super().__init__()


class Format1(Instruction):  # ppddaaaa
    def __init__(self, mnemonic, operands):
        super().__init__(mnemonic)
        # load dd [from] aaaa
        self.dest = operands[0]
        self.address = operands[1]

    def __str__(self):
        binary_string = "00"
        binary_string += format_binary(self.dest, 2)
        binary_string += format_binary(self.address, 4)
        return hex(int(binary_string, 2))[2:]


class Format2(Instruction):  # ppssaaaa
    def __init__(self, mnemonic, operands):
        super().__init__(mnemonic)
        # store ss [in] aaaa
        self.source = operands[0]
        self.address = operands

    def __str__(self):
        binary_string = "01"
        binary_string += format_binary(self.source, 2)
        binary_string += format_binary(self.address, 4)
        return hex(int(binary_string, 2))[2:]


class Format3(Instruction):  # ppddssxx
    def __init__(self, mnemonic, operands):
        super().__init__(mnemonic)
        # add dd [+] ss [and store it in dd]
        self.dest = operands[0]
        self.source = operands[1]

    def __str__(self):
        binary_string = "10"
        binary_string += format_binary(self.dest, 2)
        binary_string += format_binary(self.source, 2)
        binary_string += "00"
        return hex(int(binary_string, 2))[2:]


class Format4(Instruction):  # ppppssxx
    def __init__(self, mnemonic, operands):
        super().__init__(mnemonic)
        self.source = operands[0]

    def __str__(self):
        opcode = "1100" if self.mnemonic == "neg" else "1101"
        binary_string = opcode
        binary_string += format_binary(self.source, 2)
        binary_string += "00"
        return hex(int(binary_string, 2))[2:]


class Format5(Instruction):  # ppppssaa
    def __init__(self, mnemonic, operands):
        # out source [to IO] aa
        super().__init__(mnemonic)
        self.source = operands[0]
        self.address = operands[1]

    def __str__(self):
        binary_string = "1110"
        binary_string += format_binary(self.source, 2)
        binary_string += format_binary(self.address, 2)
        return hex(int(binary_string, 2))[2:]


class Format6(Instruction):  # ppppaaaa
    # jump [back to instruction at address] aaaa
    def __init__(self, mnemonic, operands):
        super().__init__(mnemonic)
        self.address = operands[0]

    def __str__(self):
        binary_string = "1111"
        binary_string += format_binary(self.address)
        return hex(int(binary_string, 2))[2:]


class Variable(RamContent):
    def __init__(self, name, value: int, address: int):
        super().__init__()
        self.name = name
        self.value = value
        self.address = address

    def __str__(self):
        return hex(self.value)[2:]


format_map = {
    "load": Format1,
    "store": Format2,
    "add": Format3,
    "neg": Format4,
    "shiftr": Format4,
    "out": Format5,
    "jump": Format6
}
