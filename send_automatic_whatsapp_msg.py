import pyautogui
import time 

time.sleep(5)
count=0 
while count<=2:
    #pyautogui.click()
    pyautogui.typewrite("hii" + str(count))
    pyautogui.press("enter")
    count=count+1