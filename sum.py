def line_1(x):
    return 3*x+8

def line_2(x):
    return 5*x+2

input = int(raw_input('input your x value \n'))
if line_2(input) > line_1(input):
    print("line 2 is greater")
else:
    print("line 1 is greater")
