def rgb_to_hex(rgb):

    hex_code = '#'

    splitted_rgbs = rgb.replace('rgb', '').replace('(', '').replace(')', '').replace(' ', '').split(',')

    for rgb_code in splitted_rgbs:
        hex_code += str(hex(int(rgb_code))[2:]).rjust(2, '0')

    return hex_code



print(rgb_to_hex("rgb(255, 255, 255)"))
print(rgb_to_hex("rgb(1, 11, 111)"))
print(rgb_to_hex("rgb(173, 216, 230)"))
print(rgb_to_hex("rgb(79, 123, 201)"))