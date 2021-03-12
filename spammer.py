import pyautogui, time
time.sleep(5)
f = open("beemoviescript.txt", "r")

#while True:
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(1)