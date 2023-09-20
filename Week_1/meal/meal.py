def main():
    time = input("What time is it? ")
    decimaltime=convert(time)
    if(decimaltime >= 7 and decimaltime <= 8):
        print("breakfast time")
    elif(decimaltime >= 12 and decimaltime <= 13):
        print("lunch time")
    elif(decimaltime >= 18 and decimaltime <= 19):
        print("dinner time")


def convert(time):
    hour,minute =time.split(":")
    hour= int(hour)
    minute=int(minute)
    decimaltime = hour + (minute/60)
    return decimaltime


if __name__ == "__main__":



    main()