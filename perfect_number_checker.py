try:
    s=int(input("enter the number: "))
    a=list(range(1,s))
    m=[]
    for i in a:
        if s%i==0:
            m.append(i)
    k=sum(m)
    if k == s:
        print(s,"is a perfect number")
    else:
        print(s,"is not a perfect number")
    
except Exception:
    print("invalid Input. give a valid input")

else:
    print("Done!")
finally:
    print("command executed!")
