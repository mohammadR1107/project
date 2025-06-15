from data import*
from action import*
import random
word = random.choice(words)
print(word)
fill_line(word)
print(line)
c = 0
while True:
    letter =input("enter a letter: ")
    indexes = find_letter_in_word(word,letter)
    if len(indexes) == 0:
        print(HANGMANPICS[c])
        c = c+1
    else:
        replace_latter(letter,indexes)
    if loose(c) == False:
        print("YOU LOOSE")
        break
    if win():
        print("YOU WIN")
        break
    print(line)
