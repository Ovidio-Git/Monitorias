import pyautogui, webbrowser, time

def run():
    target_number="+573002484003"
    msg = ["holo","prro","te escribo","dese un bot que programe xd"]
    webbrowser.open("https://web.whatsapp.com/send?phone="+target_number)
    time.sleep(5)
    for i in range(100):
        for i in range(4):
            pyautogui.write(msg[i])
            pyautogui.press("enter")

if __name__=='__main__':
    run()