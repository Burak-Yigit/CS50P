import inflect
mylist=[]
p = inflect.engine()
text = "Adieu, adieu, to "
while True:
    try:
        name = input("Name: ")
        mylist.append(name)
        names_string = p.join(mylist)
    except EOFError:
        print(text + names_string)
        break