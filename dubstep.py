def song_decoder(song):
    s=song.replace('WUB'," ")
    if(s[0]==" "):
        s=s[1:]
    if(s[len(s)-1]==" "):
        s=s[:len(s)-1]
    res = s.split()
    f=""
    for i in res:
        f=f+i+" "
    return f[:len(f)-1]