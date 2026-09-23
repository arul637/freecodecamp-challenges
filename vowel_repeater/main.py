def repeat_vowels(string: str) -> str:
	
	vowel_offset = 0
	vowels = 'aeiouAEIOU'
	
	result: str = ''
	
	for character in string:
		if character in vowels:
			result += character+(vowel_offset*character.lower())
			vowel_offset += 1
		else:
			result += character

	return result


print(repeat_vowels("hello world"))
print(repeat_vowels("freeCodeCamp"))
print(repeat_vowels("AEIOU"))
print(repeat_vowels("I like eating ice cream in Iceland"))