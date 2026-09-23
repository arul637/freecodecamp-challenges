def reverse_sentence(sentence):

    words = []

    word = ''
    for character in sentence: 
        if character != ' ':
            word += character
        else:
            if word != '':
                words += [word]
                word = ''

    if word:
        words += [word]

    return ' '.join(words[::-1])

print(reverse_sentence("world hello"))
print(reverse_sentence("push commit git"))
print(reverse_sentence("npm  install   apt    sudo"))
print(reverse_sentence("import    default   function  export"))