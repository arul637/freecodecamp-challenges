def solution(string: str) -> str:
    stack = [] 

    for character in string:
        if character == ')':
            new_stack = []
            while True:
                poped_character = stack.pop() 
                if poped_character == '(':
                    break 
                new_stack.append(poped_character)
            for char in new_stack:
                stack.append(char)

            continue

        stack.append(character)

    return ''.join(stack)

print(solution('(f(b(dc)e)a)'))
print(solution('((is?)(a(t d)h)e(n y( uo)r)aC)'))
print(solution('f(Ce(re))o((e(aC)m)d)p'))
