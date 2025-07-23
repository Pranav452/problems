
def custom_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

def custom_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result

def custom_reduce(func, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            accumulator = next(it)
        except StopIteration:
            raise TypeError('custom_reduce() of empty sequence with no initial value')
    else:
        accumulator = initializer
    for item in it:
        accumulator = func(accumulator, item)
    return accumulator

# Example usage:

# Transform: Square each number
numbers = [1, 2, 3, 4, 5]
squared = custom_map(lambda x: x ** 2, numbers)
print("Squared:", squared)  # Output: [1, 4, 9, 16, 25]

# Filter: Keep only even numbers
evens = custom_filter(lambda x: x % 2 == 0, numbers)
print("Evens:", evens)  # Output: [2, 4]

# Reduce: Sum all numbers
total = custom_reduce(lambda x, y: x + y, numbers)
print("Sum:", total)  # Output: 15

# Reduce with initializer: Multiply all numbers, starting from 1
product = custom_reduce(lambda x, y: x * y, numbers, 1)
print("Product:", product)  # Output: 120

