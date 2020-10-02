def calcSum(n):
    if n == 0:
        return n
    return n + calcSum(n - 2)

end = int(input("ending integer"))
print(calcSum(end))

