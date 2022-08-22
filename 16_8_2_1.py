greetings= "hello hi good bro morning evening night"

if "bro" in greetings:
    print("greetings are incorrect")
    print(" Correct greetings are : ")
    new_greetings= greetings[: greetings.index("bro")] + greetings[(greetings.index("bro")+1 + len("bro")):]
    print(new_greetings)
else:
    print("correct greetings")