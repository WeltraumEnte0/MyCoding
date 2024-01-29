import pyautogui 

def find_coordinates():
    while True:

        location = pyautogui.position()
        print(location) 
    
    

def function():
    
    menu = (1719, 19)
    newtab = (1527, 143)
    likebutton = (448, 370)
    close = (1901, 8)
    
    
    pyautogui.click(1719, 19)
    pyautogui.PAUSE = 5
    pyautogui.click(1527, 143)
    pyautogui.PAUSE = 5
    #pyautogui.typewrite('https://www.sportabzeichen-wettbewerb.de/wettbewerbsbeitrag/wettbewerbsbeitrag-227/', interval=0.05)
    pyautogui.press('strg', 'v')
    pyautogui.PAUSE = 5
    pyautogui.click('enter')
    pyautogui.PAUSE = 5
    pyautogui.press(448, 370)
    pyautogui.PAUSE = 5
    pyautogui.press(1901, 8)
    pyautogui.PAUSE = 5
    
        
function()
    
    
    
    