import pyautogui
import time 

time.sleep(5)
count=0 
while count<=n:   # n= number of times you want to send message
    #pyautogui.click() / you can use this if you want to automate clicks. For  specific position you need to specify location(x and y coordinates)
    pyautogui.typewrite("Your Message")
    pyautogui.press("enter")
    count=count+1
    
_________________________________________________________________________________________________________________________________________________________________________

#example:    n=2
#            pyautogui.typewrite("Hii" + str(count))

#output:     Hii 0
#            Hii 1
#            Hii 2
  
    
