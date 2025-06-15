from data import*
def fill_line(words):
    for x in words:
        line.append("-")
def find_letter_in_word(word,letter):
    indexes = []
    c = 0
    for x in word:
        if x == letter:
            indexes.append(c)
        c +=1
    return indexes
def replace_latter(letter,indexes):
    for x in indexes:
        line[x] = letter
def loose(c):
    if c > 6 :
        return False
    else:
        return True
def win():
    for x in line:
        if x=="-":
            return False
    return True