def rangoli(integer):
    if integer<27 and integer>0:
        string=""
        width=(integer*4)-3
        char=""
        joined=""
        for i in range(1,integer+1):
            char=chr(integer-i+97)
            joined=joined[:(len(joined)+1)//2]+ char + joined[(len(joined))//2::-1]
            dashed= "-".join(joined)
            string=string+dashed.center(width,"-")+"\n"
        rev=string.split("\n")
        joined2=""
        exclude=rev[:len(rev)-2]
        for i in reversed(exclude):
            if i==exclude[0]:
                joined2=joined2+ i
            else:
                joined2=joined2+ i+ "\n"
        string=string+ joined2
    print(string)
integer=int(input())
rangoli(integer)