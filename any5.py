def unpopular_letter(filename):
    f=open(filename, "r")
    c=f.read()
    
    dict={}
    for i in c:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    
    return max(dict, key = dict.get)

print(unpopular_letter("any100.txt"))