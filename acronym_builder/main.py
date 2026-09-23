def build_acronym(s: str):

    ignore_words = ['a', 'for', 'an', 'and', 'by', 'of']

    splitted_string = s.split(' ')

    result = ''

    for word in splitted_string:
        if word in ignore_words:
            continue 

        result += word[0].upper() 

    return result 


print(build_acronym("Search Engine Optimization"))
print(build_acronym("Frequently Asked Questions"))