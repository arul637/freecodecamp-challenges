def all_unique(s):

    unique_container = set() 

    for character in s:
        if character not in unique_container:
            unique_container.add(character)
        else:
            return False 

    return True 


print(all_unique("abc"))
print(all_unique("aA"))
print(all_unique("QwErTy123!@"))
print(all_unique("~!@#$%^&*()_+"))
print(all_unique("hello"))
print(all_unique("freeCodeCamp"))
print(all_unique("!@#*$%^&*()aA"))