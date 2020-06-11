def openOrSenior(data):
    l=[]
    for i in range(len(data)):
        if(data[i][0]>=55 and data[i][1]>7):
            l.append("Senior")
        else:
            l.append("Open")
    return l