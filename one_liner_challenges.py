# 1. List of cubes of odd numbers from 1 to 15
cubes_of_odds = [x**3 for x in range(1, 16) if x % 2 == 1]
print("Cubes of odd numbers from 1 to 15:", cubes_of_odds)

# 2. Filter out all strings with length > 3 from a list
words = ['cat', 'lion', 'tiger', 'rat', 'bat', 'elephant']
short_words = list(filter(lambda w: len(w) <= 3, words))
print("Words with length <= 3:", short_words)

# 3. Concatenate a list of strings into a single string using reduce
from functools import reduce
strs = ['one', 'liner', 'challenge']
concatenated = reduce(lambda a, b: a + b, strs)
print("Concatenated string:", concatenated)

# 4. Get the squares of numbers divisible by 3 from 1 to 20
squares_div3 = list(map(lambda x: x**2, filter(lambda x: x % 3 == 0, range(1, 21))))
print("Squares of numbers divisible by 3 from 1 to 20:", squares_div3)

# 5. Convert a list of temperatures in Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print("Celsius to Fahrenheit:", fahrenheit)
