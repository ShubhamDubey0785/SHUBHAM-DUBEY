a=int(input())
b=int(input())
def fun(a,b):
    if a%2==0 and b%2==0:
        if a>b:
            print(b)
        else:
            print(a)
    else:
        if a>b:
            print(a)
        else:
            print(b)
fun(a,b)
