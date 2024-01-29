def list():
  thislist = ["apple", "banana", "cherry"]
  thislist[1:2] = ["blackcurrant", "watermelon"]
  print(thislist)
  print(thislist[2])
  thislist[3] = "horst"
  z = thislist[3]
  print(z)





list()

def test():
  
    list = []
    for i in range(100):
        list.append(i+1)

    b = 0
    #for z in range(50):

    #erhöhen der primzahl
    prim = list[b]
    
    print(list)

    for i in list:
        a = prim
        list[a] = "x"
        a = a + prim
    print(list)
test()