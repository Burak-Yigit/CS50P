def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    punctuations = [",", "?", ".", "!"]
    if len(s) < 2 or len(s) > 6:
        return False
    for char in s:
        if char in punctuations:
            return False
    if s.isdigit():
        return False
    if len(s) == 4 and s[2] == '0':
        return False
    if len(s) == 6 and s[3] == '0':
        return False
    return True

if __name__ == "__main__":
    main()









