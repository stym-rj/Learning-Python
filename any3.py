def relation(horiz, vert):
    if(len(horiz)!=len(vert)):      #base condition
        return -1
    
    M=[]
    for i in vert:
        M1=[]
        for j in horiz:
            if j%i==0:
                M1.append(1)
            else:
                M1.append(0)
        M.append(M1)

    return M

h=[1,20,5,4,6]
v=[4,8,11,100,2]
print(relation(h,v))