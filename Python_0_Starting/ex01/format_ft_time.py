import datetime
import time


def main():
    current_date = datetime.date.today().strftime("%B %d %Y")
    epoch = datetime.datetime(1970, 1, 1)
    epoch = datetime.datetime.strftime(epoch, "%B %d, %Y")
    print("Seconds since " + epoch + ': ' + str(time.time()) +
          '  or ' + f"{time.time():.2e}" + ' in scientific notation')
    print(current_date)


main()
