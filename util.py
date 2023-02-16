
def format_binary(n: int, width: int):
    out = bin(n)[2:]
    zeros = width - len(out)
    out = "0" * zeros + out
    return out
