import tkinter
from tkinter import RIGHT, END, DISABLED # right, end, disabled
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
            font=display_font, justify='right',
            bg=white_green, width=50, borderwidth=5,
        )
        display.pack(padx=5, pady=5)
        
        # button widgets
        def r_b(text, bg=light_green, **kwards):
            button = tkinter.Button(button_frame,
                text=text, font=button_font, bg=bg, **kwards
            )
            return button
        
        clear_button = r_b('Clear', dark_green, command=lambda: [display.delete(0, tkinter.END), decimal_button.config(state='normal')])
        quit_button = r_b('Quit', dark_green, command=self.destroy)     
        
        inverse_button = r_b('1/x')
        square_button = r_b('x^2')
        exponent_button = r_b('x^n')
        divide_button = r_b(' / ')
        multiply_button = r_b('*')
        substract_button = r_b('-')
        add_button = r_b('+')
        equal_button = r_b('=', dark_green)
        decimal_button = r_b('.', 'black', fg='white', command=lambda:self.submit_number('.'))
        negate_button = r_b('+/-', 'black', fg='white')
        
        num_buttons = [r_b(str(i),'black', fg='white', command=lambda num=i :self.submit_number(num)) for i in range(10)] 
        
        # 1st row
        clear_button.grid(row=0, column=0, columnspan=2, pady=1, sticky='WE')
        quit_button.grid(row=0, column=2, columnspan=2 ,pady=1, sticky='WE')
        
        def grid_em(items, row, **kwards):
            for column, item in enumerate(items):
                item.grid(row=row, column=column, pady=1, sticky='WE', **kwards)
        
        # 2nd row
        grid_em(items=[inverse_button, square_button, exponent_button, divide_button], row=1)
        # 3rd row, add padding to create the size of the columns "ipadx"
        grid_em(items=[*num_buttons[7:], multiply_button], row=2, ipadx=20)
        # 4th row
        grid_em(items=[*num_buttons[4:7], substract_button], row=3)
        # 5th row
        grid_em(items=[*num_buttons[1:4], add_button], row=4)
        # 6th row
        grid_em(items=[negate_button, num_buttons[0], decimal_button, equal_button], row=5)
        
        self.display = display
        self.decimal_button = decimal_button
    # end def make_layout
    
    def submit_number(self, number):
        '''Add a numbert or decimal to the display'''
        # insert numbert was pressed and if decimal disable the widget
        self.display.insert('end', number)
        
        if '.' in self.display.get():
            self.decimal_button.config(state='disabled')
    
    def run(self):
        self.make_layout()
        self.mainloop()

Calculator().run()
