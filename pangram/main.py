def is_pangram(sentence, letters):

    sentence_set = set() 
    letters_set = set() 

    for character in sentence:
        if character not in sentence_set:
            if not character.isalpha():
                continue
            sentence_set.add(character.lower())

    for character in letters:
        if character not in letters_set:
            if not character.isalpha():
                continue
            letters_set.add(character.lower())

    return len(list(sentence_set)) == len(list(letters_set))



print(is_pangram("hello", "helo"))
print(is_pangram("hello", "hel"))
print(is_pangram("hello", "helow"))
print(is_pangram("hello world", "helowrd"))
print(is_pangram("Hello World!", "helowrd"))
print(is_pangram("Hello World!", "heliowrd"))
print(is_pangram("freeCodeCamp", "frcdmp"))
print(is_pangram("The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"))