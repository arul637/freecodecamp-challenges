from typing import Dict 

def frequency_calculator(string: str) -> Dict:
    dictionary: Dict = {}

    for character in string:
        if character.isalpha():
            if character in dictionary:
                    dictionary[character.lower()] += 1
            else:
                    dictionary[character.lower()] = 1

    return dictionary


def are_anagrams(string1: str, string2: str) -> bool:
    return frequency_calculator(string1) == frequency_calculator(string2)


print(are_anagrams("listen", "silent"))
print(are_anagrams("School master", "The classroom"))
print(are_anagrams("A gentleman", "Elegant man"))
print(are_anagrams("Hello", "World"))
print(are_anagrams("apple", "banana"))
print(are_anagrams("cat", "dog"))