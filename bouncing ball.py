def bouncingBall(h, bounce, window):
    if(h>0):
        if(bounce>0 and bounce<1):
            if(window<h):
                c=1
                while(h>window):
                    c+=2
                    h=h*bounce
                return c-2
    return -1