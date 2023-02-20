###############--WORD GUESSING GAME--###############
####################################################

#====================================#
#  Opens the list file
#====================================#
file = open('textfile2.txt', 'r')
words = file.readlines()

#====================================#
#  Removes escape character from list
#====================================#
cleanList = []
for word in words:
    cleanList.append(word.strip())
length_of_list = len(cleanList)
#print(length_of_list)

#====================================#
#  Sets up random number
#====================================#
from lib2to3.pytree import LeafPattern
import random
n = random.randint(1,length_of_list)
#print(n)

#====================================#
#  Chooses random word from list
#====================================#
for x in cleanList[0:n]:
    randomword = x
#print(randomword)


#====================================#
#  Guessing the word
#====================================#
no_guesses = 0
loop = True 
print('\nPick a word from the list below:')    
print(cleanList)
while loop: #can also use: while loop == True:
    guess = input('\nGuess the word: ').lower()
    no_guesses = no_guesses + 1
    if guess == randomword.lower():
        loop = False
        print('Correct!')
        if no_guesses == 1:
            print(f'Wow!! You only needed {no_guesses} guess!\n')
        elif no_guesses > 5:
            print(f"You're not very good at this, it took you {no_guesses} guesses!\n")
        else:
            print(f'You needed {no_guesses} guesses!\n')
        break
    else:
        print('Incorrect, try again!')

