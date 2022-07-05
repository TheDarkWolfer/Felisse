import pyautogui, time, qrcode, random

def fill_form(name:str,mail:str,message:str):
    pyautogui.alert("5s delay before filling the form \n Click 'ok' to start timer")
    time.sleep(5)
    pyautogui.typewrite(name,interval=0.1)
    pyautogui.press("tab")
    pyautogui.typewrite(mail,interval=0.1)
    pyautogui.press("tab")
    pyautogui.typewrite(message,interval=0.1)
    pyautogui.press("enter")

def make_qr_code(qrData:str):
    img = qrcode.make(qrData)
    qrName = f"qr_code_{str(random.randint(100000,999999))}.png"
    img.save(qrName)
    return qrName


def toolkit(id=int(input("Tool ID :>"))):
    if id == 1:
        fill_form()
    elif id == 2:
        make_qr_code(qrData=str(input("Enter the qr code data :>")))


while True:
    toolkit()
