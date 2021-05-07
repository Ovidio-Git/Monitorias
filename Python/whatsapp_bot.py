import pyautogui, webbrowser, time

def run():

    print(
    """
            ________
           /_______/
           \ \    / /	    _           _
         ___\ \__/_/___    | |__   ___ | |_
        /____\ \______/\   | '_ \ / _ \| __|
        \ \   \/ /   / /   | |_) | (_) | |
         \ \  / /\  / /    |____/ \___/\__|
          \ \/ /\ \/ /
           \_\/  \_\/

    """)

    # request numbers for send sms
    target_number=input(
    """
        Ingrese el numero al que desea escribir:
        (Ej : +573000000)
        
        -> """)

    msg = input("\n\r"+" "*8+"Ingrese el mensaje que desea enviar:\n\r"+" "*8+"-> ")
    target_number.replace(" ", "")
    frecuency = int(input("\n\r"+" "*8 +"Cuantas veces desea enviar el mensaje:\n\r"+" "*8+"-> "))

    # connect to whatsapp web
    webbrowser.open("https://web.whatsapp.com/send?phone="+target_number)
    time.sleep(5)

    # sending message
    for i in range(frecuency):
        pyautogui.write(msg)
        pyautogui.press("enter")
    print("\n\r"+" "*8+"que se siente el spam perro?[FINISHED PROGRAM]")

if __name__=='__main__':
    run()