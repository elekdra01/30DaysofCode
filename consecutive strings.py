def longest_consec(strarr, k):
    s=""
    l=[]
    for i in range(len(strarr)-k+1):
        for j in range(i,i+k):
            s+=strarr[j]
        l.append(len(s))
        s=""
    if(len(l)!=0):
        l=l.index(max(l))
        for i in range(l,l+k):
            s+=strarr[i]
        return s
    else:
        return 