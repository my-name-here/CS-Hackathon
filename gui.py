import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk as ttk
def run_python_file():
    import subprocess
    subprocess.call(['python', 'testtesttest.py'])
class TinterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Object Detection Demo")
        
        height = 700
        width = int(.75*height)
        self.geometry(f"{width}x{height}")  
        self.eval('tk::PlaceWindow . center')
        self.background_image = Image.open("gradient.jpeg") 
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.place(x=0, y=0)


        self.logo_image = Image.open("logo.png")
        self.logo_image.thumbnail((96,96),Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo_photo).pack(pady=(height/2.5,5))



        self.button = ttk.Button(self, text="Start App", command=run_python_file)
        self.button.pack()
        
if __name__ == "__main__":
    app = TinterApp()  
    app.mainloop()