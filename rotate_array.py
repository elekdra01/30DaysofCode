t=int(input())
for _ in range(t):
    n,r=input().split()
    l= list(map(int, input().split()))
    r=int(r)
    l=l[r:]+l[0:r]
    s=""
    for i in l:
        s+=str(i)+" "
    print(s)
    l=[]