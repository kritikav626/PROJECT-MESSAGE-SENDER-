'''---IT'S A PROJECT ON MESSAGE_SENDER  WHICH HELPS YOU TO RECIEVE OTP'S SMS FROM  PEOPLE...'''
import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo,showerror

def send_sms(number,message):
    url = "https://www.fast2sms.com/dev/bulk"
    params = {
        'authorization' : "9MIPR2LUzOIvBZwlcTG4dPCHtUhW1VQcTemwySo1JhebjhCbYaKppCqsTgQ6",
        'sender_id' : "FSTSMS",
        'message'  :  message,
        'language' :  "english",
        'route' :  "p",
        'numbers' : number
    }
    response = requests.get(url, params=params)
    dict = response.json()
    print(dict)
    return dict.get('return')

'''------function calling for send sms button conncetivity-----'''
def btn_click(): #access the details like number and text message from user---
    num = textnumber.get()
    mesg = textmesg.get('1.0',END)
    r = send_sms(num, mesg)
    if r == True:
        showinfo('message sent','successfully sent')
    else:
        showerror('error','something went wrong..')

#CREATING GUI WITH THE HELP OF TKINTER :----
root =Tk()
root.title('Message Sender')
root.geometry("400x550")
font = ('Helvetica',20,'bold')

'''------TAKE VARIABLES FOR INPUT TEXT NUMBER AND FOR MESSAGE IN SENDING BOX-------'''
textnumber = Entry(root, font=font)
textnumber.pack(fill=X, pady=20) #it will text inside the given axis form start to end----

textmesg = Text(root)
textmesg.pack(fill=X)


Sendbtn = Button(root, text='SEND SMS', command=btn_click)
Sendbtn.pack()

root.mainloop() #it will create user interface......