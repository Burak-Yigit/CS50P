def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(text):


    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    message_without_vowels=""
    for i in range(len(text)):
        if text [i] not in vowels:
            message_without_vowels += text[i]

    return message_without_vowels


if __name__ == "__main__":
    main()
