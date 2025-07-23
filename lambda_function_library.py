from math import factorial


square = lambda x: x**2
print(square(5))

add = lambda x,y: x+y
print(add(5,6))

is_even = lambda x: x%2==0
print(is_even(5))

is_positive = lambda x: x>0
print(is_positive(-5))

factorial = lambda x: factorial(x)
print(factorial(5))

fibonacci = lambda x: fibonacci(x-1) + fibonacci(x-2) if x>1 else x
print(fibonacci(5))

is_prime = lambda x: all(x%i!=0 for i in range(2,x))
print(is_prime(5))

is_palindrome = lambda x: x == x[::-1]
print(is_palindrome("madam"))

is_anagram = lambda x,y: sorted(x) == sorted(y)
print(is_anagram("listen", "silent"))


reverse = lambda x: x[::-1]
print(reverse("hello"))







