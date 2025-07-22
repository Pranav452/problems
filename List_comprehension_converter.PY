squares = []
for i in range(10):
    squares.append(i*i)
print(squares)
evens =[i for i in range(10) if i % 2 == 0]
odd_even=["even" if i % 2 == 0 else "odd" for i in range(10)]
print(odd_even)

fibonacci = [i for i in range(10) if i % 2 == 0]
print(fibonacci)

#convert to list comprehension
# squares = []
# for i in range(10):
#     squares.append(i*i)
# print(squares)
# evens =[i for i in range(10) if i % 2 == 0]