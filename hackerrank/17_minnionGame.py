def minion_game(string):
    p1="Stuart"
    sp1=0
    wp1=""
    p2="Kevin"
    wp2=""
    sp2=0
    if len(string)>0 and len(string)<=1000000:
        for i in range(len(string)):
            if string[i] in "AEIOU":
                sp2+=len(string)-i
            else:
                sp1+=len(string)-i

        if sp1>sp2:
            print(p1 + " " + str(sp1))
        elif sp2>sp1:
            print(p2 + " " + str(sp2))
        else:
            print("Draw")

s="BANANA"
minion_game(s)