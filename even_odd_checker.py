def odd_even_checker(x):
    a=str(x)
    for i in a:
        i=int(i)
        if i==0:
            print(i,"is zero")
        elif i%2==0:
            print(i,"is even number")
        else:
            print(i,"it's odd number")
