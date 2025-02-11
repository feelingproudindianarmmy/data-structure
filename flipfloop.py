a=[1,2,3,3,2,1]
s=0
e=len(a)-1
while s>e:
    if (a[s]!=a[e]):
        return False
    s=s+1
    e=e-1
return True
r=[3,6,4,4,6,3]
if palen(r):
    print("It is a flip flop")
else:
    print("It is not a flip flop")