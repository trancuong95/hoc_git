def f(n):
    if n == 0:
        return 0
    else:
        return f(n-1)+100
# Bài Python 65, Code by Quantrimang.com


n = int(input("Nhập số n>0: "))
print(f(n))
