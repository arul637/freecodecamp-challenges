def handle(string):
    output = ''
    for character in string:
        if character.isalpha():
            output += character
        else:
            continue 
        
    return output 

def is_mirror(str1, str2):

    string = handle(str1) + handle(str2)

    i=0
    j=len(string)-1

    while i<j:
        if string[i] != string[j]:
            return False 
        i+=1
        j-=1

    return True

    
print(is_mirror("helloworld", "helloworld"))
print(is_mirror("Hello World", "dlroW olleH"))
print(is_mirror("RaceCar", "raCecaR"))
print(is_mirror("RaceCar", "RaceCar"))
print(is_mirror("Mirror", "rorrim"))
print(is_mirror("Hello World", "dlroW-olleH"))
print(is_mirror("Hello World", "!dlroW !olleH"))