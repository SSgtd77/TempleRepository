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

def print_lst(lst):
    if isinstance(lst, list):
        for index, val in enumerate(lst):
            print(f"{index} - {val}")
    else:
        print(f"{lst} is not list")


if __name__ == "__main__":
    print_text("Hello Fucing World!")
    print_text(125)
    print("-------")
    print_int(258)
    print_int("Hello")
    print("-------")
    print_flt(5.26)
    print_flt(5)
    print("-------")
    lst = [num for num in range(1, 5)]
    print_lst(lst)
    print_lst(50)
    