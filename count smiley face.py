def count_smileys(arr):
    c=0
    for i in range(len(arr)):
        l=len(arr[i])
        if(l==2):
            if(arr[i][0]==':' or arr[i][0]==';'):
                if(arr[i][1]==')' or arr[i][1]=='D'):
                    c+=1
        elif(l==3):
            if(arr[i][0]==':' or arr[i][0]==';'):
                if(arr[i][1]=='-' or arr[i][1]=='~'):
                    if( arr[i][2]==')' or arr[i][2]=='D'):
                        c+=1
    return c