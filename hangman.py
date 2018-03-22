from __future__ import print_function
import random

word_bank = ['overwatch','destiny','fortnite','call of duty',
    'grand theft auto','doom','battlefield','league of legends',
    'hearthstone','rainbow six siege','street fighter','dark souls']
print ('''
    _
   | |                                            
   | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
   | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
   | | | | (_| | | | | (_| | | | | | | (_| | | | |
   |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |                      
                      |___/      
    ''')
print('')

print('Welcome to hangman! This is a hangman game that involves a theme of \
popular videogame franchises and videogames in recent times.'
' Please guess only one letter at a time. Please enter in lower case only. ')
print('')

# We intialize 6 turns, because of the head, body, arms, and legs.
turns = 6
secretword = random.choice(word_bank)
print('For testing purposes: the mystery word/phrase is', secretword)
print('I have a word with',len(secretword),'characters.')

def hangman_display(guessed, secret):
    """This takes your guesses and nulls whatever is not in the secret word. 
    The guessed contains all of your guesses
    
    """
    result = ''
    #This is for the display function
    for letter in secret:
        if letter in guessed:
            letter = letter
            result += letter
        elif letter == ' ':
            letter = ' '
            result += letter
        else:
            letter = '_ '
            result += letter
    print(result)
    return result
    
    
def hangman():
    ''' This is the main function in the game that takes user input to determine
    a random word in the word bank. Next, the user says a letter that will run
    through the function that then adds it to the word/phrase'''
    turns = 6
    total = ''
    guessed = []
    count = len(secretword)
    win_condition = ''
    #while loop runs when you are alive.
    while turns > 0:
        print('')
        guess = raw_input('Guess a letter: ').lower()
        print('')
        for letter in guess:
            if len(guess) > 1:
                print('You can not put more than 1 letter!')
                break
            if letter in guessed:
                print('You already guessed that!')
            elif letter in secretword:
                count -= 1
                total += letter
                win_condition = hangman_display(total, secretword)
                guessed.append(letter)
            else:
                win_condition = hangman_display(total, secretword)
                guessed.append(letter)
        if win_condition == secretword:
            print('')
            print('\033[32m Congratulations, You won! \n')
            print('''
 __   __                                
 \ \ / /                                
  \ V /___  _   _     __      _____  _ __  
   \ // _ \| | | |    \ \ /\ / / _ \| '_ \ 
   | | (_) | |_| |     \ V  V / (_) | | | |
   \_/\___/ \__,_|      \_/\_/ \___/|_| |_|
                                       
                                       
   
'''    )
            
            break
            
        if guess not in secretword:
                turns -= 1
                print('')
                print('Wrong')
                print('')
                print('You have',turns,'lives left.')
                print('')
                if turns == 0:
                    print('\033[31m The word was', secretword, end='. \n')
                    print('')
                    print('\033[31m Game Over. \n')
                    print('''
   _____                         ____                 
  / ____|                       / __ \                
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ''')
            
           
hangman()