#using join() method, we can join all the substrings of a string with another substring.

text1=" ".join(["this", "is", "the", "material"])
print(text1)
text2="...".join(["this", "is", "the", "material"])
print(text2)

text3="this is a song"
text4="--".join(text3)
print(text4)

text5=["this", "is", "a", "dragon"]
print(text5)
print(text5[0])
print(text5[1])
text6="**".join(text5)
print(text6)
print("".join(text5))

text7=["this is a normal string"]
text8="START now"
text9=text8.join(text7)
print(text9)

text10="this is good"
print("-".join(text10))