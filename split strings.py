def solution(s):
    if(len(s)%2==1):
        s=s+'_'
    print(s)
    l=[]
    for i in range(0,len(s),2):
        l.append(s[i:i+2])
        
    return l    
    pass