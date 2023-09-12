def hello():
    text= input()
    words = text.split()
    wordsWithDots="...".join(words)
    print(wordsWithDots)

hello()