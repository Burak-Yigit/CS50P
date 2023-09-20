camel_case = input("camelCase: ")
to_snake_case =""

for i in camel_case:
    if(i.isupper()):
        to_snake_case+="_"+i.lower()
    else:
        to_snake_case+=i

print(to_snake_case)
