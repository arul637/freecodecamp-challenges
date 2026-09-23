def get_laptop_cost(laptops, budget):
    laptops.append(budget)
    laptops = sorted(list(set(laptops)))[::-1]    

    index = laptops.index(budget)

    if laptops[-1] == budget:
            return 0
    elif index == 0:
        return laptops[2]
    else:
        return laptops[index+1]
    


print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))
print(get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900))
print(get_laptop_cost([2099, 1599, 1899, 1499], 2200))
print(get_laptop_cost([2099, 1599, 1899, 1499], 1000))
print(get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450))