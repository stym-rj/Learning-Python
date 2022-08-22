message="Acer pretator helios 300"      #in this string, the word 'predator' is written wrong.
#so to fix that, :
# message[8]="d"      #this will give error

#this is how we do this:
new_message=message[:8]+ "d" + message[9:]      #this will do the work.
print(new_message)

text="hello brooooo"
print(text)
text="hello hello"
print(text)