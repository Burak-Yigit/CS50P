import random

def main():
    level= get_level()
    score = 0
    attempt = 0
    question = 0
    x,y =  generate_integer(level)
    while True:
         try:
             answer = int(input(f"{x} + {y} = "))
             if answer == x+y:
                  score+=1

                  x,y =  generate_integer(level)
                  question+=1
                  if question == 10:
                       print(f"Score: {score}")

                       break
             else:
                  attempt+=1
                  print("EEE")
                  if attempt == 3:
                       attempt = 0
                       print(f"{x} + {y} = {x+y}")
                       question+=1
                       x,y =  generate_integer(level)
         except ValueError:
             print("EEE")

def get_level():
        while True:
             try:
                level = int(input("Level: "))

                if level <= 0 or level > 3:
                    continue
                else:
                    return level
             except ValueError:
                 pass


def generate_integer(level):
    x = 0
    y = 0
    if level == 1:
         x = random.randint(0,9)
         y = random.randint(0,9)
         return x,y
    elif level == 2:
         x = random.randint(10,99)
         y = random.randint(10,99)
         return x,y
    elif level == 3:
         x = random.randint(100,999)
         y = random.randint(100,999)
         return x,y
if __name__ == "__main__":
    main()