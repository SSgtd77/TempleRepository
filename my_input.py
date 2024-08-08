LINE=5

def input_text():
    inputTxt = input("Enter any string: ")
    if isinstance(inputTxt, str):
        print(f"You input: {inputTxt}")
    else:
        print(f"{inputTxt} is not string")

if __name__ == "__main__":
    input_text()
    