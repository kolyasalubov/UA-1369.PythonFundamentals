word_from_user = input("Enter your word\n ")

def calculate_characters(word_from_user):
    char_count = {}
    for i in word_from_user.lower():
        char_count[i] = char_count.get(i, 0) + 1
    return char_count

print(calculate_characters(word_from_user))