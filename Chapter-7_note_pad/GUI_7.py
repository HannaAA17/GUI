import tkinter
from PIL import Image, ImageTk

class Notepad(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Notepad')
        self.iconbitmap('pad.ico')
        self.geometry('600x600')
        self.resizable(0, 0)
    # end def __init__

    def define_layout(self):
        
        # region Define fonts and colors
        text_color = "#fffacd"
        menu_color = "#dbd9db"
        root_color = "#6c809a"
        
        self.config(bg=root_color)
        # endregion Define fonts and colors
        
        # region Define Frames
        menu_frame = tkinter.Frame(self, bg=menu_color)
        text_frame = tkinter.Frame(self, bg=text_color)
        menu_frame.pack(padx=5, pady=5)
        text_frame.pack(padx=5, pady=5)
        # endregion Define Frames
        
        # region Functions
        def new_note():
            pass
        
        def open_note():
            pass
        
        def save_note():
            pass
        
        def close_note():
            pass
        # endregion Functions
        
        # region Create the menu: new, open, save, close
        new_image = ImageTk.PhotoImage(Image.open('new.png'))
        new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
        new_button.grid(row=0, column=0, padx=5, pady=5)
        
        open_image = ImageTk.PhotoImage(Image.open('open.png'))
        open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
        open_button.grid(row=0, column=1, padx=5, pady=5)
        
        save_image = ImageTk.PhotoImage(Image.open('save.png'))
        save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
        save_button.grid(row=0, column=2, padx=5, pady=5)
        
        close_image = ImageTk.PhotoImage(Image.open('close.png'))
        close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
        close_button.grid(row=0, column=3, padx=5, pady=5)
        
        # to keep the images from disappearing
        self.images = [new_image, open_image, save_image, close_image]
        # endregion Create the menu: new, open, save, close
        
        # regionCreate the menu: font family, font size, font option
        
        # endregionCreate the menu: font family, font size, font option
        
    # end def define_layout
        
    def run(self):
        self.define_layout()
        self.mainloop()
Notepad().run()