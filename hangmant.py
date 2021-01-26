#Hangman part one
import random

def hangman():
    words = ['rat', 'hat', 'bat']
    rndm = random.randint(0, 2)
    selection = words[rndm]
    wrong = 0
    stages = ['',\
              '_______       ',\
              '|             ',\
              '|      |      ',\
              '|      0      ',\
              '|     /|\     ',\
              '|     / \     ',\
              '|             ',]
    rletters = list(selection)
    board = ['__'] * len(selection)
    win = False
    print('suh cuh play hangman')

#hangman part two

    while wrong < len(stages) - 1:
        print('\n')
        msg = ('Guess a letter cuh')
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '__' not in board:
            print('victory cuh')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('pathetic cuh. the word was {}.'.format(selection))
