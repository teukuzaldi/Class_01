# 1. List values
#
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
#
# You need to do two separate things here and report both in your Python file.
# You should have two solutions in this file, one for item 1 and one for item 2.
# Item 2 is tricky so if you get stuck try your best (no penalty), for a hint check out the solution by desiato here.
#
#     Make a new list that has all the elements less than 5 from this list in it and print out this new list.
#     Write this in one line of Python (you do not need to append to a list just print the output).
# __________________________________________________________

list = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]  #the first tasks
new_list = [i for i in list if i < 5]
print(new_list)

print([i for i in list if i < 5])  #the second tasks

# __________________________________________________________
# 2. List overlap
#
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
#
#     Determine which items are present in both lists.
#     Determine which items do not overlap in the lists.

#___________________________________________________________

list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']

both_lists = set(list_a) & set(list_b)
non_overlap = set(list_a) ^ set(list_b)
print(both_lists)  #tasks 1
print(non_overlap)  #tasks 2

#__________________________________________________________
#
# 3. Given a singe phrase, count the occurrence of each word
#
# Using this string:
#
# string = 'hi dee hi how are you mr dee'
#
#     Count the occurrence of each word, and print the word plus the count
#     (hint, you might want to "split" this into a list by a white space: " ").
#
#______________________________________________

string = 'hi dee hi how are you mr dee'
words = string.split(' ')
word_count = {}

for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1
for i, count in word_count.items():
    print(f'the word {i} is appears {count} times')

#______________________________________________
# 4. User input
#
# Ask the user for an input of their current age,
# and tell them how many years until they reach retirement (65 years old).
#
# Hint:
#
# age = input("What is your age? ")
# print "Your age is " + str(age)

input_age = int(input("What is your age? "))
retired = 65
years_until_retirement = retired - input_age

print(f'You have {years_until_retirement} years until retirement.')

# 5. User input 2
#
# Using the following dictionary (or a similar one you found on the internet),
# ask the user for a word, and compute the Scrabble word score for that word
# (Scrabble is a word game, where players make words from letters, each letter is worth a point value),
# steal this code from the internet, format it and make it work:
#
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }
#_______________________________________________________________________________________
letter_scores = {"aeioulnrst": 1,"dg": 2,"bcmp": 3,"fhvwy": 4,"k": 5,"jx": 8,"qz": 10}

put_your_scrible_word = input("What is your scrable? ")
score = 0
for i in put_your_scrible_word:
    for key in letter_scores:
        if i in key: score += letter_scores[key]

print(f'your scrable word score of "{put_your_scrible_word}" is {score}.')
# ______________________________________________________________________________________

# https://www.geeksforgeeks.org/python-program-to-implement-jumbled-word-game/

import random


# function for choosing random word.
def choose():
    # list of word
    words = ['rainbow', 'computer', 'science', 'programming',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']

    # choice() method randomly choose
    # any word from the list.
    pick = random.choice(words)

    return pick


# Function for shuffling the
# characters of the chosen word.
def jumble(word):
    # sample() method shuffling the characters of the word
    random_word = random.sample(word, len(word))

    # join() method join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled


# Function for showing final score.
def thank(p1n, p2n, p1, p2):
    print(p1n, 'Your score is :', p1)
    print(p2n, 'Your score is :', p2)

    # check_win() function calling
    check_win(p1n, p2n, p1, p2)

    print('Thanks for playing...')


# Function for declaring winner
def check_win(player1, player2, p1score, p2score):
    if p1score > p2score:
        print("winner is :", player1)
    elif p2score > p1score:
        print("winner is :", player2)
    else:
        print("Draw..Well Played guys..")


# Function for playing the game.
def play():
    # enter player1 and player2 name
    p1name = input("player 1, Please enter your name :")
    p2name = input("Player 2 , Please enter your name: ")

    # variable for counting score.
    pp1 = 0
    pp2 = 0

    # variable for counting turn
    turn = 0

    # keep looping
    while True:

        # choose() function calling
        picked_word = choose()

        # jumble() function calling
        qn = jumble(picked_word)
        print("jumbled word is :", qn)

        # checking turn is odd or even
        if turn % 2 == 0:

            # if turn no. is even
            # player1 turn
            print(p1name, 'Your Turn.')

            ans = input("what is in your mind? ")

            # checking ans is equal to picked_word or not
            if ans == picked_word:

                # incremented by 1
                pp1 += 1

                print('Your score is :', pp1)
                turn += 1

            else:
                print("Better luck next time ..")

                # player 2 turn
                print(p2name, 'Your turn.')

                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp2 += 1
                    print("Your Score is :", pp2)

                else:
                    print("Better luck next time...correct word is :", picked_word)

                c = int(input("press 1 to continue and 0 to quit :"))

                # checking the c is equal to 0 or not
                # if c is equal to 0 then break out
                # of the while loop o/w keep looping.
                if c == 0:
                    # thank() function calling
                    thank(p1name, p2name, pp1, pp2)
                    break

        else:

            # if turn no. is odd
            # player2 turn
            print(p2name, 'Your turn.')
            ans = input('what is in your mind? ')

            if ans == picked_word:
                pp2 += 1
                print("Your Score is :", pp2)
                turn += 1

            else:
                print("Better luck next time.. :")
                print(p1name, 'Your turn.')
                ans = input('what is in your mind? ')

                if ans == picked_word:
                    pp1 += 1
                    print("Your Score is :", pp1)

                else:
                    print("Better luck next time...correct word is :", picked_word)

                    c = int(input("press 1 to continue and 0 to quit :"))

                    if c == 0:
                        # thank() function calling
                        thank(p1name, p2name, pp1, pp2)
                        break

            c = int(input("press 1 to continue and 0 to quit :"))
            if c == 0:
                # thank() function calling
                thank(p1name, p2name, pp1, pp2)
                break


# Driver code
if __name__ == '__main__':
    # play() function calling
    play()

# https://www.geeksforgeeks.org/python-program-to-implement-jumbled-word-game/ i found the scramble code from this website