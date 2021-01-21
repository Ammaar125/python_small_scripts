from random import shuffle # importing shuffle function from random library.
def player_guess(): # defining a function for player guess.
    
    guess=''
    
    while guess not in['0','1','2']:
        guess=input("Enter the number between 0,1 and 2: ")
        
    return int(guess)  

def ball_shuffler(mylist): # defining a function for ball shuffling
    
    shuffle(mylist)
    
    return mylist

def guess_checker(shuffled_list,guess): # defining a function for the our guess checking
    
    if shuffled_list[guess]=='0':
        print("your guess is right you won")
    
    else:
        print("wrong guess, you lost")
        print(shuffled_list)

# we'll start game by welcoming player
print("Welcome to guess game. you have to guess and tellus where the glass is")

# balls hidden in glasses images.
print("    ----   "+"   "+"    ----   "+"   "+"    ----   ")   
print("   /    \  "+"   "+"   /    \  "+"   "+"   /    \  ")  
print("  /      \ "+"   "+"  /      \ "+"   "+"  /      \ ") 

# intializing with a list.
mylist=['','','0']

# starting with a guess.
guess=player_guess()

# shuffling the ball.
shuffled_list=ball_shuffler(mylist)

# checking the guess.
guess_checker(shuffled_list,guess)