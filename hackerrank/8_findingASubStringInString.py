def count_substring(string, sub_string):
    if len(string)<=200:
        appearence=string.count(sub_string)
        return appearence

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)