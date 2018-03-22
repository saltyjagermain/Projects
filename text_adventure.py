from __future__ import print_function

print('\033[31m Disclaimer: Everything needs to be spelled correctly or else '
'it will not work, thank you. \n')

print('\033[01m Act 1: The Key \n')

print('\033[94m You wake up and feel slightly light headed. You realize you are' 
' inside a dimmly lit room with a small amount of sunlight bleeding in through \
a small window. \n')
#The Raw Input in these functions
def firstquestions():
    '''This is the first question about using brute force'''
    force = raw_input('\033[94m You see a metal door, would you like to try and '
    'break it down? (Yes or No): \n')
    return force
 
def secondquestions():
    '''This is the second question about choosing an object to view'''
    look3 = raw_input('\033[94m You look around the room, it is musky and damp.'
    'You notice a "filing cabinet", a "desk", a broken "clock" that is stuck at' 
    '2:46, a "rug", and a rusty "air vent". What do you check first?: \n')
    return look3
    
def thirdq():
    '''This is the third question about choosing which the key goes in'''
    key2 = raw_input('\033[94m The key can open a lock in the room.You need to \
    find on which object the key works. Here are your options: "file", "drawer",\
    "door" : \n')
    return key2
    
def coins():
    '''If you call this function you escaped as this is a secret ending'''
    print('\033[34m You climb on top of the desk to use the coins to unscrew the'
    'air vent and escape! \n')

def fourthq():
    '''This fourth question chooses what the second key goes in?'''
    key3=raw_input('\033[94m The key can go in the file or the door. '
    'Choose wisely: ')
    return key3

def fifthq():
    '''The last question asks a riddle if you have made it this far'''
    riddle=raw_input('\033[94m The key goes in the door which then leads you to '
    'another room. It takes a correct answer to this riddle to escape. '
    'The riddle is "What has holes, but can hold water?": ')
    return riddle

def door(): 
    '''This is the main function that has all of the conditionals'''
    force=firstquestions()
    if force == 'Yes' or force == 'yes' or force == 'y' or force == 'Y':
        print ('\033[31m You ram your shoulder into the metal door, it does not ' 
    'budge. \n')
    else:
        print('You choose better, the door looks pretty sturdy')

def act1_2q():
    '''This function is for if you got the question wrong, instead of repeating
    the same output, we decided to change it.'''
    tryagain1 = raw_input('\033[94m That did not seem to be helpful, '
    'try picking something else.Your options are "rug","clock","air vent","wind\
    ow,","filing cabinet": ')
    return tryagain1

def misund():
    '''A function to say a response was not understood'''
    print('Sorry, I did not understand your response.')
#This is the Act1
def act1():
    '''This is the first scene that decides what to do if you get the question 
    right or wrong.'''
    look3 = secondquestions()
    if look3 != 'filing cabinet':
        if look3 != 'window':
            if look3 != 'clock':
                if look3 != 'rug':
                    if look3 != 'desk':
                        if look3 != 'air vent':
                            misund()
                            act1_2()
                        else:
                            print('The air vent is screwed tight into the wall.')
                            act1_2()
                    else:
                        print('There is some old papers that are mostly blank, '
                        'but, you also find a couple of coins.')
                        act1_2()
                else:
                    print('\033[34m You lift up the rug and find a small copper '
                    'key wedged inbetween the boards. \n')
                    act2()
            else:
                print('You look at the clock closely, you find nothing useful.')
                act1_2()
        else:
            print('The window is too high for you to reach.')
            act1_2()
    else:
        print('The filing cabinet has lots of damp papers, the top cabinet is '
        'locked')
        act1_2()
        
def act1_2():
    '''This function is for if they get the question wrong, it outputs what 
    is needed for that response.'''
    look3 = act1_2q()
    if look3 != 'filing cabinet':
        if look3 != 'window':
            if look3 != 'clock':
                if look3 != 'rug':
                    if look3 != 'desk':
                        if look3 != 'air vent':
                            print('Sorry, I did not understand your response.')
                            act1_2()
                        else:
                            print('The air vent is screwed tight into the wall.')
                            act1_2()
                    else:
                        print('There is some old papers that are mostly blank, '
                        'but, you also find a couple of coins.')
                        act1_2()
                else:
                    print('\033[34m You lift up the rug and find a small copper '
                    'key wedged inbetween the boards. \n')
                    act2()
            else:
                print('You look at the clock closely, you find nothing useful.')
                act1_2()
        else:
            print('The window is too high for you to reach.')
            act1_2()
    else:
        print('The filing cabinet has lots of damp papers, the top cabinet is '
        'locked')
        act1_2()
#This is for Act2

def act2():
    '''This is the second act where you have to find where the key goes in'''
    print('\033[31m Act 2: The Key Strikes Back \n')
    key2 = thirdq()
    if key2 == 'file':
        print('The key is broken from the inside of the lock.')
        print('\033[31m Game Over \n')
    if key2 == 'door':
        print('Sorry, the key is too small.')
        act2_2()
    if key2 == 'drawer':
        print('You find a clue, "The Bell Tolls at Midnight, you walk over '
        'to the clock and change the time to midnight, a key falls out and '
        'into your hand.')
        act3()
    if key2 == 'coins':
        coins()

def act2_2():
    '''This is the second act that changes the output when you choose wrong'''
    key2 = raw_input(' ')
    if key2 != 'file':
        if key2 != 'door':
            if key2 != 'drawer':
                misund()
            else:
                print('You find a clue, "The Bell Tolls at Midnight, you walk over '
                'to the clock and change the time to midnight, a key falls out and '
                'into your hand.')
                act3()
        else:
            print('The key is too small to fit inside the lock.')
            act2_2()
    else:
        print('The key is broken inside of the lock.')
        print('\033[31m Game Over \n')
    if key2 == 'coins':
        coins()
#This is for Act3

def act3():
    '''The third act is for which the second key goes in'''
    print('\033[31m Act 3: The Key (Really? Another Key?) \n')
    key3=fourthq()
    if key3 != 'door':
        if key3 != 'file':
            misund()
        else:
            print('You find a medium sized key inside.')
            act4()
    else:
        print('The key does not fit')
        act3_1()
    if key3 == 'coins':
        coins()

def act3_1():
    '''The third act is for which the second key goes in'''
    key3 = raw_input(' ')
    if key3 != 'door':
        if key3 != 'file':
            misund()
        else:
            print('You find a medium sized key inside.') 
            act4()
    else:
        print('The key does not fit')
        act3_1()
    if key3 == 'coins':
        coins()
#This is the last act

def act4():
    '''The last act is if you get this riddle right you escape otherwise you 
    lose'''
    print('\033[31m Act 4: The Riddle \n')
    riddle=fifthq()
    if riddle=='sponge':
        print('\033[34m Congratulations! You escaped !\n')
    else:
        print('\033[31m A large spike pops up from the ground and impales you. '
        'The end. \n')
        
door()
act1()
