a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: x**2, filter(lambda i: i % 2 == 0, a))))
