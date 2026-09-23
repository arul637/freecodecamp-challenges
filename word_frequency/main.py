def get_words(paragraph):
    frequency = {}
    words = paragraph.split()
    punctuation = ',.!'

    for word in words:
        cutted_word = word

        for p in punctuation:
            cutted_word = cutted_word.replace(p, '')

        cutted_word = cutted_word.lower()

        if cutted_word not in frequency:
            frequency[cutted_word] = 1
        else:
            frequency[cutted_word] += 1

    output = []

    for key, value in frequency.items():
        output.append((value, key))

    output = sorted(output, key=lambda x: x[0], reverse=True)

    result = []

    for i in output[:3]:
        result.append(i[-1])

    return result

print(get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding"))
print(get_words("I like coding. I like testing. I love debugging!"))
print(get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!"))