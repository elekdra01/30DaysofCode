#code
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()[:n]))
    for i in range(0, n): 
        for j in range(0, n): 
            if (a[j] == i + 1): 
                print(j + 1, end = " ") 
                break
    print()
