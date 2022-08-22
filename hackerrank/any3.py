def minion_game(string):
    p1="Stuart"
    sp1=0
    wp1=""
    p2="Kevin"
    wp2=""
    sp2=0
    if len(string)>0 and len(string)<=1000000:
        count1=0
        count2=0
        for i in string:
            count1=count1+1
            count2=count2+1
            if (i!="A" and i!="E" and i!="I" and i!="O" and i!="U"):
                if count1==len(string):
                    wp1=wp1 + string[count1-1:]
                else:
                    temp=string[count1-1:]
                    wp1=wp1 + string[count1-1:]+ " "
                for j in range(len(temp)-1):
                    wp1=wp1 + string[count1-1: len(string)-1-j]+ " "
            elif (i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
                if count2==len(string):
                    wp2=wp2 + string[count2-1:]
                else:
                    temp=string[count2-1:]
                    wp2=wp2 + string[count2-1:]+ " "
                for j in range(len(temp)-1):
                    wp2=wp2 + string[count2-1: len(string)-1-j]+ " "
        lp1=wp1.split(" ")
        sp1=len(lp1)
        lp2=wp2.split(" ")
        sp2=len(lp2)

        if sp1>sp2:
            print(p1 + " " + str(sp1-1))
        elif sp2>sp1:
            print(p2 + " " + str(sp2-1))
        else:
            print("Draw")
            


s="BANANA"
minion_game(s)