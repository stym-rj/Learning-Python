#to find how many letters are present in a string.

def count_letters(string):
    result={}
    for letter in string:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result

print(count_letters("aaaaaaaaaaaa"))
print(count_letters("aaabcbbrbcder"))
print(count_letters("satyam rajjj"))