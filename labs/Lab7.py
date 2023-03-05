import pyautogui

screenW, screenH = pyautogui.size()

print("Do you wanna know your screen size(width and height)? click any key")
if str(input()) != "":
    print('your screen size is %s and %s' % (screenW,screenH))

print("Wanna see some magic: ")
if str(input()) != "":
    print("your mouse is gone!")
    pyautogui.move(2000, 0, duration=2)

print("Write a command and I will type and execute it for you!")
pyautogui.write(str(input()))
pyautogui.press('enter')
