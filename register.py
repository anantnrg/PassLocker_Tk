from tkinter import *
from tkinter import ttk


class Register(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Main = master
        self.init_window()

    def init_window(self):
        self.Main.title("Register - PassLocker v3.0")
        self.Main.iconbitmap(r'login.ico')
        self.pack(fill=BOTH, expand=1)

        # Variables
        passwd_txt = "\u2022"

        # Functions
        def btn_register_click():
            print(rb_value.get())
            print(txtbox_name.get())
            print(txtbox_usrname.get())
            print(txtbox_email.get())
            print(txtbox_passwd.get())
            self.quit()

        # Fixing Fonts
        style = ttk.Style(root)
        style.configure("TRadiobutton", font=('Ubuntu', 12))
        btn_style = ttk.Style(root)
        btn_style.configure("TButton", font=('Ubuntu', 12))

        # Labels
        lbl_name = Label(root, text='Name', font=('Ubuntu', 14))
        lbl_name.place(x=80, y=40)
        lbl_email = Label(root, text='Email Address', font=('Ubuntu', 14))
        lbl_email.place(x=80, y=100)
        lbl_usrname = Label(root, text='User Name', font=('Ubuntu', 14))
        lbl_usrname.place(x=80, y=160)
        lbl_passwd = Label(root, text='Master Password', font=('Ubuntu', 14))
        lbl_passwd.place(x=80, y=220)

        # Text Boxes
        txtbox_name = ttk.Entry(root, font=('Ubuntu', 14))
        txtbox_name.place(x=240, y=40)
        txtbox_email = ttk.Entry(root, font=('Ubuntu', 14))
        txtbox_email.place(x=240, y=100)
        txtbox_usrname = ttk.Entry(root, font=('Ubuntu', 14))
        txtbox_usrname.place(x=240, y=160)
        txtbox_passwd = ttk.Entry(root, font=('Ubuntu', 14), show=passwd_txt)
        txtbox_passwd.place(x=240, y=220)

        # Check Boxes
        rb_value = StringVar()
        set_given_email_as_default_for_entries = ttk.Radiobutton(root, text='Use the given email address as default '
                                                                            'email for all entries', style='TRadiobutton', value='use_given_email_for_all_entries', variable=rb_value)
        set_given_email_as_default_for_entries.place(x=60, y=280)
        use_different_email_for_different_entries = ttk.Radiobutton(root, text='Use different email addresses for '
                                                                               'different entries', style='TRadiobutton', value='do_not_use_given_email_for_all_entries', variable=rb_value)
        use_different_email_for_different_entries.place(x=60, y=310)

        # Buttons
        btn_cancel = ttk.Button(root, text="Cancel", style='TButton', command=root.quit)
        btn_cancel.place(x=120, y=380)
        btn_register = ttk.Button(root, text="Register", style='TButton', command=btn_register_click)
        btn_register.place(x=320, y=380)


root = Tk()
root.geometry("550x440")
app = Register(root)
root.mainloop()
