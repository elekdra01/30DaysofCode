def unique_in_order(iterable):
    l=[]
    for i in range(len(iterable)):
        if (iterable[i] not in l):
            l.append(iterable[i])
        else:
            if(l[len(l)-1]!=iterable[i]):
                l.append(iterable[i])
    return l
    pass