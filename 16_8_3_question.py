#if there is a word present in the string as 'car', replace the 'car' and write '(car will not be included here here)'

def check(text):
    if "car" in text:
        print(text[:text.index("car")]+ "(car will not be included here)" + text[text.index("car")+len("car"):])
    else:
        print(text)

text1="bike cycle bro car man laptop"
text2="bike cycle bro clocktower man laptop"
check(text1)
check(text2)