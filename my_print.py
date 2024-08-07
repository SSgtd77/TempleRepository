def print_text(txt):
    if isinstance(txt, str):
        print(txt)
    else:
        print(f"{txt} is not string")

def print_int(number):
    if isinstance(number, int):
        print(number)
    else:
        print(f"{number} is not integer")

def print_flt(flt):
    if isinstance(flt, float):
        print(flt)
    else:
        print(f"{flt} is not float")


if __name__ == "__main__":
    print_text("Hello Fucing World!")
    print_text(125)
    print("-------")
    print_int(258)
    print_int("Hello")
    print("-------")
    print_flt(5.26)
    print_flt(5)
