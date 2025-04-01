word = input("Enter your word -> ")

def calculate_characters(word):
    char_count = {}
    for i in word:
        char_count[i] = char_count.get(i, 0) + 1
    return char_count

print(calculate_characters(word))