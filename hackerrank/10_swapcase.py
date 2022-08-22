def swap_case(s):
    swap=""
    for i in range(len(s)):
        if s[i].lower()==s[i]:
            swap=swap+s[i].upper()
        elif s[i].upper()==s[i]:
            swap=swap+s[i].lower()
    return swap
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)