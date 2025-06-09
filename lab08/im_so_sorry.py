def blocks(n):
    if n <= 0:
        return 0
    else:
        return blocks(n - 1) + n # longer version of the function

    def blocks(n): #shorter version of the function
        return 0 if n <= 0 else blocks(n-1) + n

print(blocks(9))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(2))