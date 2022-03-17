import tkinter

class Calclator(tkinter.Tk):
    # colors
    dark_green = '#93af22'
    light_green = '#acc253'
    white_green = '#edefe0'
    
    # fonts
    button_font = ('Arial', 18)
    display_font = ('Arial', 30)
    
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.iconbitmap('calc.ico')
        self.geometry('300x400')
        self.resizable(0, 0)
    # end def __init__

    def make_layout(self):
        # frames
        display_frame = tkinter.LabelFrame(self)
        button_frame = tkinter.LabelFrame(self)
        
        display_frame.pack()
        button_frame.pack()
        
        # layout widgets
        display = tkinter.Entry(display_frame, font=Calclator.display_font, justify=tkinter.RIGHT, bg=Calclator.white_green, width=50, borderwidth=5)
        display.pack(padx=5, pady=5)
        

    def run(self):
        self.make_layout()
        self.mainloop()

Calclator().run()
