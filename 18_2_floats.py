price=7.6535
tax=price*1.345
print("The item w/o tax is {} dollors and with tax its {} dollors.".format(price, tax))
print("The item w/o tax is {price} dollors and with tax its {tax} dollors.".format(price=price, tax=price*1.345))
print("The item w/o tax is {:.2f} dollors and with tax its {:.3f} dollors.".format(price, tax))
# print("The item w/o tax is {:.2f(price)} dollors and with tax its {:.3f(tax)} dollors.".format(price=price, tax=price*1.345))       #WRONG.no such thing.
print("The item w/o tax is {price:.2f} dollors and with tax its {tax:.3f} dollors.".format(price=price, tax=tax))