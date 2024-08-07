def hello_world():
    print("Hello World!")


def print_text(txt):
    if isinstance(txt, str):
        print(txt)
    else:
        print(f"{txt} is not string")


if __name__ == "__main__":
    hello_world()
    print_text("Hello Fucing World!")
    print_text(125)

