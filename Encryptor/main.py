encryptordict = {

}

for letter in "abcdefghijklmnopqrstuvwxyz":
    encryptordict[letter]= input(f"Enter the coded value for {letter}: ")


while True:
    phrase = input("Enter the text for encoding: ")
    encodedPhrase = ""

    for letter in phrase:
        if letter != " ":
            encodedPhrase = encodedPhrase + encryptordict[letter]
        else:
            encodedPhrase = encodedPhrase + letter

    print(encodedPhrase)
    