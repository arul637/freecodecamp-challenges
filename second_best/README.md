Given an array of integers representing the price of different laptops, and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.

## Examples 

```
1. get_laptop_cost([1500, 2000, 1800, 1400], 1900) should return 1800
2. get_laptop_cost([1500, 2000, 2000, 1800, 1400], 1900) should return 1800
3. get_laptop_cost([2099, 1599, 1899, 1499], 2200) should return 1899
4. get_laptop_cost([2099, 1599, 1899, 1499], 1000) should return 0
5. get_laptop_cost([1200, 1500, 1600, 1800, 1400, 2000], 1450) should return 1400
```