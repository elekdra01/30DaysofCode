def likes(names):
    l=len(names)
    if(l==0):
        v="no one likes this"
        return v
    elif(l==1):
        v=str(names[0])+" likes this"
        return v
    elif(l==2):
        v=str(names[0])+" and "+str(names[1])+" like this"
        return v
    elif(l==3):
        v=str(names[0])+", "+str(names[1])+" and "+str(names[2])+" like this"
        return v
    else:
        l=l-2
        v=str(names[0])+", "+str(names[1])+" and "+ str(l)+" others like this"
        return v