t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    s=a[0]
    for i in range(1,n):
        if(a[i]==a[i-1]):
            s+=a[i]+1
            a[i]=a[i]+1
        elif(a[i]<a[i-1]):
            d=a[i-1]-a[i]
            s+=a[i]+d+1
            a[i]=a[i]+d+1
        else:
            s+=a[i]
    print(s)