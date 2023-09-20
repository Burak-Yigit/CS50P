import random

while True:
    try:
        level_number = int(input("Level: "))
    except:
        continue
    if level_number >= 1:
        level = random.randint(1, level_number)
        break
while True:
    try:
        guess_number = int(input("Guess: "))
    except:
        continue
    if guess_number < 1:
        continue
    elif guess_number > level:
        print("Too large!")
    elif guess_number < level:
        print("Too small!")
    elif guess_number == level:
        print("Just right!")
        break