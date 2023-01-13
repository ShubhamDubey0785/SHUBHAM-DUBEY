a=input()
x="abcdefghijklmnopqrstuvwxyz"
def fun(a):
    if (a[0] and a[1]) in x:
        print(True) 
    else:
        print(False)
fun(a)