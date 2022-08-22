def print_formatted(number):
    if number>0 and number<100:
        spaces=len("{0:b}".format(number))
        formatted=""
        for i in range(1,number+1):
            string=str(i)
            decimal=string.rjust(spaces, " ")
            octal="{0:o}".format(i).rjust(spaces, " ")
            cap_hex=str("{0:x}".format(i)).upper()
            hexal=(cap_hex.rjust(spaces, " "))
            binary="{0:b}".format(i).rjust(spaces, " ")
            if i!=number:
                formatted= formatted+ decimal + " " + octal+ " " + hexal+ " " + binary+ " " + "\n"
            else:
                formatted= formatted+ decimal + " " + octal+ " " + hexal+ " " + binary
        return print(formatted)
number=int(input())
print_formatted(number)