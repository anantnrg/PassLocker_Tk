from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3


class Login(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.login_window = master
        self.init_window()

    def init_window(self):
        self.login_window.title("Master Login - PassLocker")
        self.login_window.iconbitmap(r'login.ico')
        self.pack(fill=BOTH, expand=1)
        passwd_text = "\u2022"

        # Functions
        def main():
            os.system('python main.py')
            self.quit()

        def validate():
            if len(txtbox_passwd.get()) == 0:
                messagebox.showerror(title="Error!", message="No Password provided. Please "
                                                             "provide a User Name and Password to login to PassLocker")
                txtbox_passwd.focus()
            else:
                pass
                db_validate()

        # Labels
        lbl_passwd = ttk.Label(font='Ubuntu', text='Password')
        lbl_passwd.place(x=50, y=30)

        # Textboxes
        txtbox_passwd = ttk.Entry(font='Ubuntu', show=passwd_text)
        txtbox_passwd.place(x=150, y=30)
        txtbox_passwd.focus()

        # Buttons
        cancel = ttk.Button(self, text="Cancel", command=root.destroy)
        cancel.place(x=90, y=130)
        login = ttk.Button(self, text="Login", command=validate)
        login.place(x=220, y=130)

        def db_validate():
            conn = sqlite3.connect('db/db.db')
            c = conn.cursor()

            def select_passwd_from_db():
                passwd = str(txtbox_passwd.get())
                c.execute('SELECT master_password FROM master_login')
                for row in c.fetchone():
                    passwd_in_db = row
                if passwd == passwd_in_db:
                    print("Verified")
                    self.quit()
                else:
                    print("incorrect")

            select_passwd_from_db()


root = Tk()

# size of the window
root.geometry("400x180")

app = Login(root)
root.mainloop()
