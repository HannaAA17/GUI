import tkinter
from tkinter import RIGHT
class Calculator(tkinter.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.iconbitmap('calc.ico')
        self.geometry('300x400')
        self.resizable(0, 0)
    # end def __init__

    def make_layout(self):
        # colors
        dark_green = '#93af22'
        light_green = '#acc253'
        white_green = '#edefe0'
        
        # fonts
        button_font = ('Arial', 18)
        display_font = ('Arial', 30)
        
        # frames
        display_frame = tkinter.LabelFrame(self)
        button_frame = tkinter.LabelFrame(self)
        
        display_frame.pack(padx=2, pady=(5, 20))
        button_frame.pack(padx=2, pady=5)
        
        # layout widgets
        display = tkinter.Entry(display_frame,
            font=display_font, justify=RIGHT,
            bg=white_green, width=50, borderwidth=5,
        )
        display.pack(padx=5, pady=5)
        
        # button widgets
        def r_b(text, bg=light_green, **kwards):
            button = tkinter.Button(button_frame,
                text=text, font=button_font, bg=bg, **kwards
            )
            return button
        
        clear_button = r_b('Clear', dark_green)
        quit_button = r_b('Quit', dark_green)     
        
        inverse_button = r_b('1/x')
        square_button = r_b('x^2')
        exponent_button = r_b('x^n')
        divide_button = r_b(' / ')
        multiply_button = r_b('*')
        substract_button = r_b('-')
        add_button = r_b('+')
        equal_button = r_b('=', dark_green)
        decimal_button = r_b('.', 'black', fg='white')
        negate_button = r_b('+/-', 'black', fg='white')
        
        num_buttons = [r_b(str(i),'black', fg='white') for i in range(10)] 
        
        # 1st row
        clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky='WE')
        quit_button.grid(row=0, column=2, columnspan=2 ,pady=1, sticky='WE')
        
        def grid_em(items, row, **kwards):
            for column, item in enumerate(items):
                item.grid(row=row, column=column, pady=1, sticky='WE', **kwards)
        
        # 2nd row
        inverse_button.grid(row=1, column=0, pady=1, sticky='WE')
        square_button.grid(row=1, column=1, pady=1, sticky='WE')
        exponent_button.grid(row=1, column=2, pady=1, sticky='WE')
        divide_button.grid(row=1, column=3, pady=1, sticky='WE')
        
        # 3rd row, add padding to create the size of the columns "ipadx"
        num_buttons[7].grid(row=2, column=0, pady=1, sticky='WE', ipadx=20)
        num_buttons[8].grid(row=2, column=1, pady=1, sticky='WE', ipadx=20)
        num_buttons[9].grid(row=2, column=2, pady=1, sticky='WE', ipadx=20)
        multiply_button.grid(row=2, column=3, pady=1, sticky='WE', ipadx=20)
        
        # 4th row
        num_buttons[4].grid(row=3, column=0, pady=1, sticky='WE')
        num_buttons[5].grid(row=3, column=1, pady=1, sticky='WE')
        num_buttons[6].grid(row=3, column=2, pady=1, sticky='WE')
        substract_button.grid(row=3, column=3, pady=1, sticky='WE')
        
        # 5th row
        num_buttons[1].grid(row=4, column=0, pady=1, sticky='WE')
        num_buttons[2].grid(row=4, column=1, pady=1, sticky='WE')
        num_buttons[3].grid(row=4, column=2, pady=1, sticky='WE')
        add_button.grid(row=4, column=3, pady=1, sticky='WE')
        

        # 6th row
        negate_button.grid(row=5, column=0, pady=1, sticky='WE')
        num_buttons[0].grid(row=5, column=1, pady=1, sticky='WE')
        decimal_button.grid(row=5, column=2, pady=1, sticky='WE')
        equal_button.grid(row=5, column=3, pady=1, sticky='WE')

    def run(self):
        self.make_layout()
        self.mainloop()

Calculator().run()
