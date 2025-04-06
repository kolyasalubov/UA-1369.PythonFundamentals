word = input("I need a good word, please write to me :")
def letter_counts(word):
    letter = {}
    for i in set(word):
       letter[i] = word.count(i)
    return letter

print (letter_counts(word))