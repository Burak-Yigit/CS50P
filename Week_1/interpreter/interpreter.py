expression= input("Expression: ").strip()
x, y, z = expression.split(" ")

match y:
    case "+":
        result=float(x)+float(z)
        print(result)
    case "-":
        result=float(x)-float(z)
        print(result)
    case "*":
        result=float(x)*float(z)
        print(result)
    case "/":
        match z:
            case "0":
               print("not possible")
            case _:
                result=float(x)/float(z)
                print("{:.1f}".format(result))




