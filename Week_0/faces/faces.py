
def main():
    text=input()
    text= text.replace(":)","🙂",-1)
    text= text.replace(":(","🙁",-1)
    print(text)

main()
