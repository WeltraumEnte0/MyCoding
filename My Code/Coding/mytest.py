


#for z in range(50):

#erhöhen der primzahl

"""
def primz():
    
    for y in list:
        h = (y-2)
        if h != "x":
            prim = list[h]
            change(prim)
            continue
"""


  # a > 1. vielfaches der Primzahl(prim - 2) * (X-1)

list = []
input = 50
for i in range(input):
    list.append(i+1)
list.pop(0)


while h < math.sqrt(input):
    if list[h] != 'X':  
        prim = list[h]
        change(prim)
    else:   
        h = h + 1


    

def change(prim):
    #verändern aller vielfachen von prim
    for X in range(len(list)):
            if X < input:
                a = prim * X                    
                list[a-2] = "x"
            else:
                break
        


primz()

print(list)