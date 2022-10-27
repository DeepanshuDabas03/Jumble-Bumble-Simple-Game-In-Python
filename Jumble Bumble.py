#Making code for jumble up words using random function import
import random
#using class for storing data of wins , loss and total games
class game_count:
    def __init__(self) :
        self.win=0
        self.total=0
    def winner(self):
        self.win+=1
    def tota(self):
        self.total+=1
    def record(self):
        #returning record of games played till now
        print("\033[1;36m Your total wins :",self.win)
        print("\033[1;36m Your total lost games :",self.total-self.win)
        print("\033[1;36m Total games played: ",self.total)
        return
print("Welcome to Jumble Bumble!!!\nUse your mind and unscramble the leters to make a meaningful word.\nNo rules xd")
#For using colour https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
list_of_words = [str(i) for i in input("Enter the list of words for which you want to play spelling match(guess)(Input should be space sepearated: ").split()]
# resource for random function,https://www.w3schools.com/python/module_random.asp
jumble = ""
#storing jumble words in empty string
jumbled_word = random.choice(list_of_words)
#random function for choosing a random word from list
correct_word = jumbled_word
p=game_count()
while jumbled_word:
    #using while loop to randomise the word completely
    l=len(jumbled_word)
    jumble += jumbled_word[random.randrange(l)]
    jumbled_word = jumbled_word[:random.randrange(l)] + jumbled_word[(random.randrange(l)+ 1):]
print("The jumble up word is:", jumble)
print("Now start guessing!")
guess = input("Please enter your guess: ")
while guess != correct_word:
    print("Oops,incorrect choice,please try again")
    p.tota()
    guess = input("Please enter your guess: ")
if guess == correct_word:
    print("Vola, you nailed it!")
    p.winner()
    p.tota()
    print("Thanks for playing with us:)")
    b=input("Would you like to play again? (Y/N)")
while b!="N":
    jumbled_word = random.choice(list_of_words)
    correct_word = jumbled_word
    jumble = ""
    while jumbled_word:
        l=len(jumbled_word)
        jumble += jumbled_word[random.randrange(l)]
        jumbled_word = jumbled_word[:random.randrange(l)] + jumbled_word[(random.randrange(l) + 1):]
    print("The jumble up word is:", jumble)
    print("Now start guessing again!")
    guess = input("Please enter your guess: ")
    while guess != correct_word :
        print("Oops,incorrect choice,please try again")
        p.tota()
        guess = input("Please enter your guess: ")
        if guess == correct_word:
            print("Vola, you nailed it!")
            game_count.winner(game_count)
            p.tota()
            print("Thanks for playing with us:)")
            b=input("Would you like to play again? (Y/N)")
#after completing all the games,printing data of all games played
if b=="N":
    print("Hope you had a wonderful time here. Here is your game record:-")
    p.record()
    print("If you don't mind can we take feedback from you about the game: ")
    s=input("Y/N: ")
    if s=="Y":
        try:
            starrating=int(input("On scale of 0-10 how would you rate us: "))
            assert starrating<=10
            assert starrating>=0
        except:
            print("Oops wrong input.")
    elif s=="N":
        print("Thank you have a wonderful day")
    else:
        print("wrong input")
#This code is written by Deepanshu_Dabas,Pulkit_Nargotra,Aditya_Bindlesh