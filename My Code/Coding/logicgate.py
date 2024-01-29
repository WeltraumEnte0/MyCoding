def AND(a,b):
    if a == 1 and b == 1:
        print(1)
    else:
        print(0)


def OR(a,b):
    if a == 1 or b == 1:
        print(1)
    else: 
        print(0)


def XOR(a,b):
    if a == 1 and b == 1: 
        print(0)
    elif a == 0 and b == 0:
        print(0)
    else: print(1)



def NOT(a,b):
    if a == 0 and b == 0:
        print(1)
    

def NOR(a,b):
    if a == 0 and b == 0:
        print(1)
    else: 
        print(0)


def NAND(a,b):
    if a == 0 and b == 0:
        print(1)
    else: 
        print(0)


a = 1
b = 1
AND(a,b)
OR(a,b)
XOR(a,b)
NOT(a,b)
NOR(a,b)
NAND(a,b)
