def complicated_function(a, b, c=True, d=False):
    print(a,b,c,d)
    pass

complicated_function(*[1,2], **{"c": "hello", "d": "cool"})