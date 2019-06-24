def ftoc(f):
    c = (f-32)/1.8
    return c
def ctof(c):
    f = c*1.8+32
    return f

def test():
    print("0摄氏度 = %.2f 华氏度" % ctof(0))
    print("0华氏度 = %.2f 摄食度" % ftoc(0))

test()