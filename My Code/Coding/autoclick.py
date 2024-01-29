from pyautogui import click, position

def print_position():
    while True:
        print(position())

x = 122
y = 327

def bot(x,y):
    for i in range(10):
        click(x, y)
       
    

#print_position()
bot(x, y)