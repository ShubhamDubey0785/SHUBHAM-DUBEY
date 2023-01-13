def functio(n):
    if (n==0 or n==1):
        return 1
    else:
        return functio(n)+functio(n-1)
print(functio(5))