def main():
        fraction = input("Fraction: ").strip()
        z = convert(fraction)
        indicator = gauge(z)
        print(indicator)


def convert(fraction):
    while True:
        try:

            x, y = fraction.split("/")
            x= int(x)
            y= int(y)
            if y != 0 and x <= y:
                 return (x/y)*100
        except ValueError:
            pass

def gauge(percentage):

     if percentage <=1:
         return "E"
     elif percentage>=99 and percentage <=100:
         return "F"
     elif percentage >1 and percentage < 99:
         return f"{percentage:.0f}%"
     else: main()

if __name__ == "__main__":
    main()