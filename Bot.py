import pyautogui
import time

print("\n1.Limit\n2.Unlimited\n")
choice = int(input("Enter the choice : "))

count = 0

if choice == 1:
    stmt = input("Enter the text: ")
    n = int(input('How much: '))
    time.sleep(5)
    while count <= n:
        pyautogui.typewrite(stmt)
        pyautogui.press("Enter")
        count = count + 1
elif choice == 2:
    stmt = input("Enter the text: ")
    time.sleep(5)
    while True:
        pyautogui.typewrite(stmt)
        pyautogui.press("Enter")
        count = count + 1
else:
    print("Invalid choice!!")
