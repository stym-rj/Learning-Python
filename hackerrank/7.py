# import textwrap

# def wrap(string, max_width):
#     print(textwrap.fill(string, max_width))

# string= input()
# max_width= int(input())

# wrap(string, max_width)


import textwrap

def wrap(string, max_width):
    wrapped=textwrap.fill(string, max_width)
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)