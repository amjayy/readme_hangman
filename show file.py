guessed = []

word = "Automobile"

def input_letter():
    #Allow user to input single letter as a guess
    while True:
         letter = input("Enter a letter:").upper()

         if len(letter) > 1:
             print("Please enter only a single letter.")
         elif letter.isnumeric():
             print("Please enter only letters.")
         else:
            return letter
def check_letter(letter):
    #Check to see if letter has been guessed already.
    if letter in guessed:
        print("You have already guessed that letter.")
    else:
        print("You have already guessed %s" % letter)
        guessed.append(letter)
def check_word(letter):
    if letter in word:
        print("You have guessed CORRECTLY")
    else:
        print(" You have guessed wrong.")
while True:
    print("\n**************************************************")
    print("You have guessed the following letters:")
    for i in guessed:
        print(i, end= '  ')
    print("\n**************************************************")
    letter = input_letter()
    check_letter(letter)
    check_word(letter)
    response = input("\n\nPress <Enter> to Continue, < Q> to Quit: ").upper()
    if response == ' Q ' :
        break
