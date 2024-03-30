#Nega lambda funksiya ishlatamiz?
def myfunc(n):
    return lambda a: a*n
ikkilantir=myfunc(2)
uchlantir=myfunc(3)
print(ikkilantir(5))
print(uchlantir(5))