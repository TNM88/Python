a=[1,3,5,7,4]
c=[2,4,6]
a.extend(c)
print (a)
b=a.copy()
print (b)
b.sort()
print (b)
for b in b:
    print (b)
    if b==5 :
        break
Largest=max(a)
print (Largest)