Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value is greater than any of the others.

## Example of valid outputs for a given input:

```
1. generate_hex("yellow") should return "Invalid color".
2. generate_hex("red") should return a six-character string.
3. generate_hex("red") should return a valid six-character hex color code.
4. generate_hex("red") should return a valid hex color with a higher red value than other colors.
5. Calling generate_hex("red") twice should return two different hex color values where red is dominant.
6. Calling generate_hex("green") twice should return two different hex color values where green is dominant.
7. Calling generate_hex("blue") twice should return two different hex color values where blue is dominant.
```