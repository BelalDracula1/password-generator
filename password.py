from tkinter import *
from tkinter import ttk
import random

root = Tk()
root.title("Password Generator")
window_height = 150
window_width = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def generate():
 def shuffle(string):
  temmlist = list(string)
  random.shuffle(temmlist)
  return ''.join(temmlist)
 passWord = ''
 for i in range(5):
  passWord = passWord + chr(random.randint(65,90)) + chr(random.randint(48,57))
 passWord = shuffle(passWord)
 result.set(passWord)
 print(passWord  + '\n'+ '-----------')
 
result = StringVar()
number_input = ttk.Entry(root, textvariable = result, font=('Tahoma',30,'bold'),justify='center',width=20)
number_input.pack(padx=10,pady=10,ipadx=10,ipady=10)
btn_result = ttk.Button(root,text = 'Generator New Password',command=generate)
btn_result.pack(padx=10,pady=10,ipadx=10,ipady=10)

generate()
root.mainloop()