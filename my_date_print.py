import datetime

LINE=7


def print_date():
   now = datetime.datetime.now()
   current_date = now.strftime("%Y/%m/%d")
   print(f"Current Date = {current_date}")


if __name__ == "__main__":
    print_date()
