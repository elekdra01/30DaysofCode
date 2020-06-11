def narcissistic( value ):
    s=str(value)
    v=len(s)
    sum=0
    for i in range(v):
        sum+=int(s[i])**v
    if(sum==value):
        return True
    else:
      return False