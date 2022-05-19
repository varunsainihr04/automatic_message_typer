import time
import pyautogui

print(" ")
print("                      ░█████╗░██╗░░░██╗████████╗░█████╗░███╗░░░███╗░█████╗░████████╗██╗░█████╗░")
print("                      ██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗")
print("                      ███████║██║░░░██║░░░██║░░░██║░░██║██╔████╔██║███████║░░░██║░░░██║██║░░╚═╝")
print("                      ██╔══██║██║░░░██║░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██╗")
print("                      ██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝")
print("                      ╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░")
print("                  ")
print("                            █▀▄▀█ █▀▀ █▀▀ █▀▀ █▀▀█ █▀▀▀ █▀▀ 　 █▀▀ █▀▀ █▀▀▄ █▀▀▄ █▀▀ █▀▀█") 
print("                            █─▀─█ █▀▀ ▀▀█ ▀▀█ █▄▄█ █─▀█ █▀▀ 　 ▀▀█ █▀▀ █──█ █──█ █▀▀ █▄▄▀") 
print("                            ▀───▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ ▀▀▀ 　 ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀─▀▀")
print("                  ")

msg = input("Enter No. of messages you want to send [0 to infinite] : ")
msgtxt = input(("Enter your message : "))

# main code
print( )
time.sleep(1)
print('Point your mouse cursor at the place where you want to type')
print('Your message will automatically start typing in 10s for '+ msg + ' times' )
time.sleep(12)
for i in range(int(msg)):  			
    pyautogui.typewrite(msgtxt)	 
    time.sleep(1)
    pyautogui.press("enter")

print('Message typed sucessfully')
time.sleep(10)