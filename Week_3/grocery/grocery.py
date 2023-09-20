grocery_list = {}

try:
    while True:
        item = input().strip().lower()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
except EOFError:
    pass

sorted_items = sorted(grocery_list.keys())

for item in sorted_items:
    count= grocery_list[item]
    print(f"{count} {item.upper()}")