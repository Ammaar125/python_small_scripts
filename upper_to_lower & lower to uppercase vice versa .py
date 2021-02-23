try:    
    s=str(input("enter any sentence here: "))
    upper_letter={'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O','p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}
    small_letter={'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
    m=[]
    for i in s:
        if i in upper_letter:
            m.append(upper_letter[i])
        elif i in small_letter:
            m.append(small_letter[i])
           
    a=' '.join(m)
    print("here is the your sentence with vice versa operation")
    print(s,"=",a)
except Exception:
    print("Invalid Input. only letters allowed no numbers and special charachter")

print("Done")    
