# Chapter 3: Functions

import random

def magic_eight(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very Doubtful'
    # my own addition
    else:
        return 'Sorry, I dont understand the words coming out of your mouth.'
    
r = random.randint(1,9)
fortune = magic_eight(r)
print(fortune)