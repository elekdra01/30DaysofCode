#code
t=int(input())
for _ in range(t):
    c=0
    n=int(input())
    arr=list(map(int,input().split()[:n]))
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                c+=1
    print(c)
    