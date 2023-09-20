def main():
    greeting = input("Greeting: ").lower().strip()
    reward(greeting)

def reward(g):
    if g.startswith("hello"):
        print("$0")
    elif g.startswith("h"):
        print("$20")
    else:
        print("$100")
main()