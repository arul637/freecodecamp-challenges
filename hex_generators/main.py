import random

def random_hex_code_alpahbet():
    hex_code = 'ABCDEF'
    return hex_code[random.randint(0, len(hex_code) - 1)]


def random_hex_code_number():
    hex_code = '0123456789'
    return hex_code[random.randint(0, len(hex_code) - 1)]


def generate_hex(color):
    colors = ['red', 'blue', 'green']

    if color not in colors:
        return 'Invalid color'

    match color:
        case 'red':
            output = random_hex_code_alpahbet()
            output += random_hex_code_alpahbet()
            output += random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_number()
            return output

        case 'green':
            output = random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_alpahbet()
            output += random_hex_code_alpahbet()
            output += random_hex_code_number()
            output += random_hex_code_number()
            return output

        case 'blue':
            output = random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_number()
            output += random_hex_code_alpahbet()
            output += random_hex_code_alpahbet()
            return output