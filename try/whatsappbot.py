import pyautogui
import webbrowser as wb
import time


wb.get("C:\Program Files/Google/Chrome/Application/chrome.exe %s").open("web.whatsapp.com")

time.sleep(30)


for i in range(600):
    pyautogui.press(".")
    pyautogui.press("enter")