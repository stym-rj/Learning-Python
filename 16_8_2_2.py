print("Input your greetings: ")
greetings= input()
print("your inputted greetings is: " + greetings)
print("If one of your greetings are wrong, then enter 1, else enter anyother number. :")
feedback=int(input())
if feedback==1:
    print("Input the wrong greeting. :")
    spelling= input()
    if spelling in greetings:
        print("Input the correct greeting. :")
        correction= input()
        new_greetings= greetings[: greetings.index(spelling)] +correction+ greetings[(greetings.index(spelling) + len(spelling)):]
        print("Your final inputted string is : ")
        print(new_greetings)
    else:
        print("Sorry, the greeting " + spelling +" is not found!")
else: 
    print("Your final inputted string is : ")
    print(greetings)