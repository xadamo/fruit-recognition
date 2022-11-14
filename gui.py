import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk


def reset_all():
    global app
    app.destroy()
    app = App()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Fruit Recognition')
        self.geometry('500x800')
        self.btn = tk.StringVar()
        self.resizable(False, False)
        self.choose = tk.IntVar()
        self.button1 = tk.Button(self, text='UPLOAD', width=20, command=self.show_image, font=("Times", 15, 'bold'))
        self.button1.pack()
        self.button2 = tk.Button(self, text='START', width=20, font=("Times", 15, 'bold'), command=self.run_script)
        self.button2.pack()
        self.button3 = tk.Button(self, text='RESET', width=20, font=("Times", 15, 'bold'), command=reset_all)
        self.button3.pack()
        self.model1 = tk.Radiobutton(self, text="LITERATURE MODEL", font=("Times", 15), value='literature',
                                     variable=self.btn, command=self.unselect_2)
        self.model1.pack()
        self.model2 = tk.Radiobutton(self, text="OUR MODEL", font=("Times", 15), value='our',
                                     variable=self.btn, command=self.unselect_1)
        self.model2.pack()

    def show_image(self):
        global img
        f_types = [ ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        preview1 = tk.Label(app, image=img)
        preview1.pack()

    def run_script(self):
        global new_img
        new_img = ImageTk.PhotoImage(file=new_file)
        preview2 = tk.Label(app, image=new_img)
        preview2.pack()

    def unselect_1(self):
        self.model1.deselect()

    def unselect_2(self):
        self.model2.deselect()


if __name__ == "__main__":
    new_file = 'media\\new_file.png'
    app = App()
    app.mainloop()

