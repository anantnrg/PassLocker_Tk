from tkinter import *
from tkinter import messagebox

class Main(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Main = master
        self.init_window()

    def init_window(self):
        self.Main.title("PassLocker v3.0")
        self.Main.iconbitmap(r'login.ico')
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Menu Functions
        def about():
            messagebox.showinfo(title='About PassLocker', message='PassLocker is an app in which you can store all '
                                                                  'your important passwords. It is developed by Anant'
                                                                  ' Narayan.                               '
                                                                  ' Github - https://github.com/anantnrg ')
        # Menus
        file = Menu(menu)
        file.add_command(label="New")
        file.add_command(label="Edit")
        file.add_command(label="Save")
        file.add_command(label="Settings")
        file.add_command(label="Exit", command=root.quit)
        menu.add_cascade(label="File", menu=file)
        help = Menu(menu)
        help.add_command(label="User Manual")
        help.add_command(label="About",command=about)
        menu.add_cascade(label="Help", menu=help)


root = Tk()
root.geometry("1360x700")
app = Main(root)
root.mainloop()
