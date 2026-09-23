def digits_or_letters(s):
    result = {
        'letters': 0,
        'digits': 0
    }

    for character in s:
        if character.isalpha():
            result['letters'] += 1 
        elif character.isdigit():
            result['digits'] += 1 
        else:
            continue 

    if result['letters'] == result['digits']:
        return 'tie'
    elif result['letters'] > result['digits']:
        return 'letters'
    else:
        return 'digits'

print(digits_or_letters("abc123"))
print(digits_or_letters("a1b2c3d"))
print(digits_or_letters("1a2b3c4"))
print(digits_or_letters("abc123!@#DEF"))
print(digits_or_letters("H3110 W0R1D"))
print(digits_or_letters("P455W0RD"))