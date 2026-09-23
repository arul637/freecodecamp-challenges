def camel_case(string: str) -> str:
    result: str = ''
    stack = ''
    for character in string:
        if character in [' ', '-', '_']:
            if result == '':
                result += ''.join(stack)
            else:
                result += ''.join(stack).title()

            stack = ''
            continue

        stack += character.lower()

    result += ''.join(stack).title()

    return result 


print(camel_case("HELLO WORLD"))
print(camel_case('secret agent-X'))
print(camel_case('FREE cODE cAMP'))
print(camel_case('ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk'))