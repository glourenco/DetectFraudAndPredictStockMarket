def mult(numA):
    total = 1

    for i in numA:
        total *= i
    return total

print(mult([1,2,3,4,5]))
print(mult([6,7,8,9]))