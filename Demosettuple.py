# Demosettuple.py
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
#print(a[0])

print("===튜플===")
tp = (1, 2, 3)
print(tp)
print(len(tp))
print(tp[0])
print("id: %s, name: %s" % ("kim", "김유신"))



def calc (a,b):
    return a+b, a*b


print(calc(3,4))