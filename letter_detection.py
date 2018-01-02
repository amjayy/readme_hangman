guessed = []
strike= []
correct = []


words = [ 'California', 'Champagne', 'Investigation', 'Programming', 'SourceTree', 'Pragmatic',
          'Formation', 'Formulate', 'Hyperbole', 'Victorious', 'Glory', 'Artificial', 'Glamorous', 'Shining',
          'Example', 'Troublesome', 'Algorithims', 'Superficial', 'Lavender', 'Sufficient','Evidence']
word = words.pop()
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
def strike_out():
      strike.append('I')   
      print("You have a strike")
      
def check_word(letter):
    if letter in word:
        print("You have guessed CORRECTLY")
    else:
        print(" You have guessed wrong.")
        strike_out()
        
def check_letter(letter):
    #Check to see if letter has been guessed already.
    if letter in guessed:
        print("You have already guessed that letter.")
    else:
        print("You have already guessed %s" % letter)
        guessed.append(letter)

    
    
while True:
    letter = input_letter()
    check_letter(letter)
    check_word(letter)
    print("\n*******************************************")
    print("What you have guessed so  far:")
    for i in guessed:
        print(i, end= '   ')
    print("\n*****************************************")
    print("These are your strikes.")
    for i in strike:
        print(i, end=' ')
    print("\n******************************************")
    response = input("\n\nPress <Enter> to Continue, <Q> to Quit: ").upper()
    if response == ' Q ' :   
        break
