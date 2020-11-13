decryptordict = {

}

for letter in "abcdefghijklmnopqrstuvwxyz":
    x = input(f"Enter the coded value for {letter}: ")
    decryptordict[x] = letter 


while True:
    phrase = input("Enter the text for decoding: ")
    decodedPhrase = ""

    for letter in phrase:
        if letter != " ":
            decodedPhrase = decodedPhrase + decryptordict[letter]
        else:
            decodedPhrase = decodedPhrase + letter

    print(decodedPhrase)