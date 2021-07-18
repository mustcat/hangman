def visualiseGuesses(guesses):
    if guesses == 0:
        return "\n"
    if guesses == 1:
        hangman = '''
    
    
    
    
    
    
  -----
    '''
    
    elif guesses == 2:
        hangman = '''

    |
    |
    |
    |
    |
  -----
    '''

    elif guesses == 3:
        hangman = '''
    ______
    |
    |
    |
    |
    |
  -----
'''

    elif guesses == 4:
        hangman = '''
    ______
    |    |
    |
    |
    |
    |
  -----
'''

    elif guesses == 5:
        hangman = '''
    ______
    |    |
    |    O
    |
    |
    |
  -----
'''

    elif guesses == 6:
        hangman = '''
    ______
    |    |
    |    O
    |    |
    |
    |
  -----
'''

    elif guesses == 7:
        hangman = '''
    ______
    |    |
    |    O
    |   -|
    |
    |
  -----
'''     

    elif guesses == 8:
        hangman = '''
    ______
    |    |
    |    O
    |   -|-
    |
    |
  -----
'''

    elif guesses == 9:
        hangman = '''
    ______
    |    |
    |    O
    |   -|-
    |    |
    |
  -----
'''

    elif guesses == 10:
        hangman = '''
    ______
    |    |
    |    O
    |   -|-
    |    |
    |   / 
  -----
'''

    else:
        hangman = '''
    ______
    |    |
    |    O
    |   -|-
    |    |
    |   / \\
  -----
'''
    
    return hangman

alphaAsciiTitle = '''
          _____                    _____                    _____                    _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         
        /::\____\                /::\    \                /::\____\                /::\    \                /::\____\                /::\    \                /::\____\        
       /:::/    /               /::::\    \              /::::|   |               /::::\    \              /::::|   |               /::::\    \              /::::|   |        
      /:::/    /               /::::::\    \            /:::::|   |              /::::::\    \            /:::::|   |              /::::::\    \            /:::::|   |        
     /:::/    /               /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /::::::|   |             /:::/\:::\    \          /::::::|   |        
    /:::/____/               /:::/__\:::\    \        /:::/|::|   |            /:::/  \:::\    \        /:::/|::|   |            /:::/__\:::\    \        /:::/|::|   |        
   /::::\    \              /::::\   \:::\    \      /:::/ |::|   |           /:::/    \:::\    \      /:::/ |::|   |           /::::\   \:::\    \      /:::/ |::|   |        
  /::::::\    \   _____    /::::::\   \:::\    \    /:::/  |::|   | _____    /:::/    / \:::\    \    /:::/  |::|___|______    /::::::\   \:::\    \    /:::/  |::|   | _____  
 /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \  /:::/    /   \:::\ ___\  /:::/   |::::::::\    \  /:::/\:::\   \:::\    \  /:::/   |::|   |/\    \ 
/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\/:::/____/  ___\:::|    |/:::/    |:::::::::\____\/:::/  \:::\   \:::\____\/:: /    |::|   /::\____\
\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /\:::\    \ /\  /:::|____|\::/    / ~~~~~/:::/    /\::/    \:::\  /:::/    /\::/    /|::|  /:::/    /
 \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    /  \:::\    /::\ \::/    /  \/____/      /:::/    /  \/____/ \:::\/:::/    /  \/____/ |::| /:::/    / 
          \::::::/    /            \::::::/    /           |::|/:::/    /    \:::\   \:::\ \/____/               /:::/    /            \::::::/    /           |::|/:::/    /  
           \::::/    /              \::::/    /            |::::::/    /      \:::\   \:::\____\                /:::/    /              \::::/    /            |::::::/    /   
           /:::/    /               /:::/    /             |:::::/    /        \:::\  /:::/    /               /:::/    /               /:::/    /             |:::::/    /    
          /:::/    /               /:::/    /              |::::/    /          \:::\/:::/    /               /:::/    /               /:::/    /              |::::/    /     
         /:::/    /               /:::/    /               /:::/    /            \::::::/    /               /:::/    /               /:::/    /               /:::/    /      
        /:::/    /               /:::/    /               /:::/    /              \::::/    /               /:::/    /               /:::/    /               /:::/    /       
        \::/    /                \::/    /                \::/    /                \::/____/                \::/    /                \::/    /                \::/    /        
         \/____/                  \/____/                  \/____/                                           \/____/                  \/____/                  \/____/         
                                                                                                                                                                               
'''

doomAsciiTitle = '''
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''
