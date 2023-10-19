import smtplib
from email.mime.text import MIMEText
import time
import random
import tkinter as tk
import threading
import subprocess
import webbrowser

def send_single_email():
    webbrowser.open('pygsmtp-single-send.py')

def set_email():
    webbrowser.open("recipientemail.txt")

def spam_send_email():
    webbrowser.open("pygsmtp-spam.py")

def open_directions():
    webbrowser.open("pastebin.com/nptEJ303")

root = tk.Tk()
root.title("pygsmtp v1.1")
root.geometry("640x480")

title_label = tk.Label(root, text="pygsmtp v1.1", font=("Verdana", 20))
title_label.pack(pady=8)
credits = tk.Label(root, text="made by packmastermc", font=("Verdana", 10))
credits.pack(padx=40,pady=8, anchor="sw")
contact = tk.Label(root, text="Discord: ihatecolor", font=("Verdana", 10))
contact.pack(padx=40,pady=0, anchor="sw")
warning = tk.Label(root, text="WARNING: This application is not as ", font=("Verdana", 10))
warning.pack(padx=40,pady=0, anchor="sw")
warning2 = tk.Label(root, text="straightforward as you might think.", font=("Verdana", 10))
warning2.pack(padx=40,pady=0, anchor="sw")
warning3 = tk.Label(root, text="Make sure to click 'Directions' if", font=("Verdana", 10))
warning3.pack(padx=40,pady=0, anchor="sw")
warning4 = tk.Label(root, text="this is your first time.", font=("Verdana", 10))
warning4.pack(padx=40,pady=0, anchor="sw")



button_font = ("Verdana", 12)
button = tk.Button(root, text="Send Single Email", command=send_single_email, width=20, height=1, font=button_font)
button.pack(padx=10, pady=40, anchor="se")

button_font = ("Verdana", 12)
openrec = tk.Button(root, text="Loop Send Email", command=spam_send_email, width=20, height=1, font=button_font)
openrec.pack(padx=10, pady=10, anchor="se")

button_font = ("Verdana", 12)
usageinst = tk.Button(root, text="Directions", command=open_directions, width=20, height=1, font=button_font)
usageinst.pack(padx=10, pady=10, anchor="se")

root.mainloop()