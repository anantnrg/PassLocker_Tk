from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class Register(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Main = master
        self.init_window()

    def init_window(self):
        self.Main.title("Set Master Password - PassLocker v3.0")
        self.Main.iconbitmap(r'login.ico')
        self.pack(fill=BOTH, expand=1)

        # Variables
        passwd_txt = "\u2022"

        # Functions
        def btn_register_click():
            if len(txtbox_passwd.get()) == 0:
                messagebox.showerror(title="Error!", message="No Master Password provided. Please "
                                                             "provide a New Master Password")
                txtbox_passwd.focus()
            else:

                save_to_db()
                self.quit()

        # Labels
        lbl_passwd = Label(root, text='New Master Password', font=('Ubuntu', 14))
        lbl_passwd.place(x=40, y=40)

        # Text Boxes
        txtbox_passwd = ttk.Entry(root, font=('Ubuntu', 14), show=passwd_txt)
        txtbox_passwd.place(x=280, y=40)

        # Buttons
        btn_cancel = ttk.Button(root, text="Cancel", command=root.quit)
        btn_cancel.place(x=120, y=120)
        btn_register = ttk.Button(root, text="Register", command=btn_register_click)
        btn_register.place(x=320, y=120)

        def save_to_db():
            conn = sqlite3.connect('db/db.db')
            c = conn.cursor()

            def create_table():
                c.execute('CREATE TABLE IF NOT EXISTS master_login(master_password TEXT)')

            def data_entry():
                passwd = str(txtbox_passwd.get())
                c.execute("SELECT * FROM master_login LIMIT 1")
                c.execute("UPDATE master_login SET master_password  = (?) ", (passwd,))
                conn.commit()
                c.close()
                conn.close()

            create_table()
            data_entry()


root = Tk()
root.geometry("560x200")
app = Register(root)
root.mainloop()
