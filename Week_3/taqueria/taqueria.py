food = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total_cash = 0.0
    while True:
        try:
            item_name = input("Item: ").title()
            item_price = food.get(item_name)
            if item_price is not None:
                total_cash += item_price
                print(f"Total: ${total_cash:.2f}")
        except EOFError:
            break


main()



