# x=0
# while x%2==0:
#     x=x/2

# the above code can cause infinite loop b/c when x==0, x/2 is also 0. so, to cure that, we will write the code as below:

x=0
if(x!=0):
    while x%2==0:
        x=x/2