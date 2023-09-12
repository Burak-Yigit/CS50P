def main():
    m=int(input("m: "))
    einstein(m)


def einstein(m):
    c = int(300000000)
    e=m*pow(c,2)
    print(f"E: {e} ")

main()