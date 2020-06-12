def calc_fuel(n):
    dic={}
    t=n*11
    x=t/800
    dic["lava"]=int(x)
    d=t%800
    y=d/120
    dic["blaze rod"]=int(y)
    d=d%120
    z=d/80
    dic["coal"]=int(z)
    d=d%80
    a=d/15
    dic["wood"]=int(a)
    b=d%15
    dic["stick"]=int(b)
    return dic