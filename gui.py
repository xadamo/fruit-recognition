import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk


def reset_all():
    global app
    app.destroy()
    app = App()
    app['background'] = 'lightgreen'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Fruit Recognition')
        self.geometry('700x800')
        self.rd = tk.StringVar()
        self.resizable(False, False)
        self.choose = tk.IntVar()
        self.button1 = tk.Button(self, text='UPLOAD', bg='lightgray', activebackground='green', width=15,
                                 font=("Times", 15, 'bold'), command=self.show_image)
        self.button1.grid(row = 0, column = 0, pady = 20, padx = 24, sticky='W')
        self.button2 = tk.Button(self, text='START', width=15, bg='lightgray', activebackground='green',
                                 font=("Times", 15, 'bold'), command=self.run_script)
        self.button2.grid(row = 0, column = 1, pady = 20, padx = 20, sticky='N')
        self.button3 = tk.Button(self, text='RESET', width=15, bg='lightgray', activebackground='red',
                                 font=("Times", 15, 'bold'), command=reset_all)
        self.button3.grid(row = 0, column = 2, pady = 20, padx = 20, sticky='E')
        self.radio1 = tk.Radiobutton(self, text="LITERATURE\nMODEL", bg='lightgreen', activebackground='lightgreen',
                                     font=("Times", 20), value='literature', variable=self.rd, command=self.unselect_2,
                                     width=12, relief='raised', indicatoron=False, borderwidth=4, selectcolor='green')
        self.radio1.grid(row = 1, column = 1, sticky = 'S', pady = 2)
        self.radio2 = tk.Radiobutton(self, text="OUR MODEL", bg='lightgreen', font=("Times", 20), value='our',
                                     variable=self.rd, command=self.unselect_1, activebackground='lightgreen',
                                     width=12, relief='raised', indicatoron=False, borderwidth=4, selectcolor='green')
        self.radio2.grid(row = 2, column = 1, sticky = 'S', pady = 2)

    def show_image(self):
        global img
        f_types = [ ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        preview1 = tk.Label(app, image=img, bg='lightgreen', width=220, pady=20)
        preview1.grid(row = 3, column = 1)

    def run_script(self):
        global new_img
        new_img = ImageTk.PhotoImage(file=new_file)
        preview2 = tk.Label(app, image=new_img, bg='lightgreen', width=220, pady=20)
        preview2.grid(row = 4, column = 1)

    def unselect_1(self):
        self.radio1.deselect()

    def unselect_2(self):
        self.radio2.deselect()


if __name__ == "__main__":
    new_file = 'media/new_file.png'
    app = App()
    app['background'] = 'lightgreen'
    app.mainloop()

