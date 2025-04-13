entered_word = input("Enter your word: ")

def counts_letters(entered_word):
    letters = {}
    entered_word = entered_word.lower()
    for i in entered_word:
        letters[i] = entered_word.count(i)
    return letters
   
print (counts_letters(entered_word))