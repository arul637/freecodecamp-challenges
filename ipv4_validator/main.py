def is_valid_ipv4(ipv4):
    splitted_ip = ipv4.split('.')

    if len(splitted_ip) != 4:
        return False

    for num in splitted_ip:
        if (len(num) == 2 and num.startswith('0')) or (num == ''):
            return False 
        else:
            if 0 <= int(num) <= 255:
                continue
            else:
                return False
            

    return True 

print(is_valid_ipv4("192.168.1.1"))
print(is_valid_ipv4("0.0.0.0"))
print(is_valid_ipv4("255.01.50.111"))
print(is_valid_ipv4("255.00.50.111"))
print(is_valid_ipv4("256.101.50.115"))
print(is_valid_ipv4("192.168.101."))
print(is_valid_ipv4("192168145213"))

'''
1. splitted length = 4 
2. length for each num > 2 must not start with 0
'''