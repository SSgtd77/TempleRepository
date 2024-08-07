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


if __name__ == "__main__":
    print_text("Hello Fucing World!")
    print_text(125)
    print("\n")
    print_text(258)
    print_text("Hello")

