# Edwin Camuy 2-15-23
import numpy as np
import IO
import sys


def main():
    # If no arguments are passed argv[1] and argv[2] will be "" and this saves us writing several try except blocks.
    sys.argv.append("")
    sys.argv.append("")
    path = sys.argv[1] if sys.argv[1] else "input.txt"

    # Generate "tokens"
    instructions, variables = IO.parse(path)
    instructions_str = [str(i) for i in instructions]

    # Put them in an array
    arr = np.full((16,), "00", np.dtype('U2'))
    for i, instruction in enumerate(instructions_str):
        arr[i] = instruction
    for v in variables:
        arr[v.address] = str(v)

    # Replace empty spaces with 0s
    with np.nditer(arr, op_flags=['readwrite']) as it:
        for x in it:
            x[...] = x or "0"

    # Format array
    ram_contents = IO.format_rom(arr)

    # Put it in a file
    IO.write(sys.argv[2] if sys.argv[2] else "output.txt", ram_contents)


if __name__ == "__main__":
    main()
