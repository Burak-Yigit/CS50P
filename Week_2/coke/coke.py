def main():
    amount_due = 50
    amount_as_string=""
    while amount_due > 0:
        insert_coin = int(input("Insert Coin: "))
        is_coin_correct = check_inserted_coin(insert_coin)
        if is_coin_correct and amount_due > 0:
            amount_due -= insert_coin
            if amount_due > 0:
                print(f"Amount Due: {amount_due}")
            elif amount_due <= 0:
                amount_as_string = str(amount_due).replace("-","")
                print(f"Change Owed: {amount_as_string}")
        elif not is_coin_correct:
            print(f"Amount Due: {amount_due}")

def check_inserted_coin(coin):
    if(coin == 25):
        return True
    elif(coin==10):
        return True
    elif(coin==5):
        return True
    else:
        return False

main()