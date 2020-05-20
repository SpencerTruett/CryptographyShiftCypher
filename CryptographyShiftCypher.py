answer = input("Would you like to encrypt or decrypt?: ")

if answer == "encrypt":
    letters = input("Please enter a word to encrypt: ").lower()
    shiftNumber = input("Please enter a number to use as a key: ")


    numbers = []

    for letter in letters:

      number = ord(letter) - 96 + int(shiftNumber)

      numbers.append(number)

    newLetters = []

    for number in numbers:

        newLetter = chr(ord('`')+number)

        newLetters.append(newLetter)

    separator = ''
    print("Your encrypted word is: " + separator.join(newLetters))

if answer == "decrypt":
    letters = input("Please enter a word to decrypt: ").lower()
    shiftNumber = input("Please enter a number to use as a key: ")


    numbers = []

    for letter in letters:

      number = ord(letter) - 96 - int(shiftNumber)

      numbers.append(number)

    newLetters = []

    for number in numbers:

        newLetter = chr(ord('`')+number)

        newLetters.append(newLetter)

    separator = ''
    print("Your decrypted word is: " + separator.join(newLetters))
