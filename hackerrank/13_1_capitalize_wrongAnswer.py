def solve(s):
    if len(s)>0 and len(s)<1000:
        p=s.split(" ")
        word=""
        for q in p:
            if q.isalnum():
                for i in q:
                    if i==q[0]:
                        if i=="":
                            word= word+ " "
                        else:
                            word= word+ i[0].upper() + i[1:]
                                
                    
        return word
s=input()
print(solve(s))