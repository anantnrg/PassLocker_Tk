from tkinter import *
from tkinter import ttk


class Login(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.login_window = master
        self.init_window()

    def init_window(self):
        self.login_window.title("Master Login - PassLocker")
        self.login_window.iconbitmap(r'login.ico')
        self.pack(fill=BOTH, expand=1)

        # Labels
        lbl_usr = ttk.Label(font='Ubuntu', text='User Name')
        lbl_usr.place(x=50, y=30)
        lbl_passwd = ttk.Label(font='Ubuntu', text='Password')
        lbl_passwd.place(x=50, y=70)

        # Textboxes
        txtbox_usr = ttk.Entry(font='Ubuntu')
        txtbox_usr.place(x=150, y=30)
        txtbox_passwd = ttk.Entry(font='Ubuntu')
        txtbox_passwd.place(x=150, y=70)

        # Buttons
        cancel = ttk.Button(self, text="Cancel")
        cancel.place(x=90, y=130)
        login = ttk.Button(self, text="Login")
        login.place(x=220, y=130)


root = Tk()

# size of the window
root.geometry("400x180")

app = Login(root)
root.mainloop()
