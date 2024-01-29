x = 0
y = 10 

if x or y:                      #entweder x oder y hat einen Wert > 0
    x += 1
    if not x or y:              #entweder x ist 0 oder y hat einen Wert > 0
        x+=1
    else:
        x+=2
else: x+3

print(x)







