import datetime

LINE=7


def print_time():
   now = datetime.datetime.now()
   current_time = now.strftime("%H:%M:%S")
   print(f"Current Time = {current_time}")


if __name__ == "__main__":
    print_time()
