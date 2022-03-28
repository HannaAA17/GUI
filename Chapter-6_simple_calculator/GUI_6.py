import tkinter
from tkinter import RIGHT, END, DISABLED # right, end, disabled
class Calculator(tkinter.Tk):
    
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.iconbitmap('calc.ico')
        self.geometry('300x400')
        self.resizable(0, 0)
        
        self.first_value = None
        self.operator = None
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
        
        '''create button widgets'''
        def r_b(text, bg=light_green, **kwards):
            button = tkinter.Button(button_frame,
                text=text, font=button_font, bg=bg, **kwards
            )
            return button
        
        add_button = r_b('+', command=lambda:self.submit_operator('+'))
        substract_button = r_b('-', command=lambda:self.submit_operator('-'))
        multiply_button = r_b('*', command=lambda:self.submit_operator('*'))
        divide_button = r_b(' / ', command=lambda:self.submit_operator('/'))
        
        inverse_button = r_b('1/x', command=lambda:self.submit_operator('1/x'))
        square_button = r_b('x^2', command=lambda:self.submit_operator('x**2'))
        exponent_button = r_b('x^n', command=lambda:self.submit_operator('**'))
        
        equal_button = r_b('=', dark_green, command=lambda:self.submit_operator('='))
        
        decimal_button = r_b('.', 'black', fg='white', command=lambda:self.submit_number('.'))
        negate_button = r_b('+/-', 'black', fg='white')
        
        clear_button = r_b('Clear', dark_green, command=lambda: [display.delete(0, tkinter.END), self.buttons_state()])
        quit_button = r_b('Quit', dark_green, command=self.destroy)     
        
        num_buttons = [r_b(str(i),'black', fg='white', command=lambda num=i :self.submit_number(num)) for i in range(10)] 
        
        self.state_buttons = [
            add_button, substract_button, multiply_button, divide_button,
            inverse_button, square_button, exponent_button, decimal_button
        ]
        
        
        '''place buttons'''
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
    # end def make_layout
    
    def submit_number(self, number):
        '''Add a numbert or decimal to the display'''
        # insert numbert was pressed and if decimal disable the widget
        self.display.insert('end', number)
        
        if '.' in self.display.get():
            self.state_buttons[-1].config(state='disabled')
    # end def submit_number
    
    def submit_operator(self, operator):
        operators = ['+','-','*','/','**','1/x','x**2','=']
        
        current_value = self.display.get()
        self.display.delete(0, tkinter.END)

        if operator in  ['1/x', 'x**2']:
            current_value = round(eval(operator.replace('x', current_value)),4)
        
        elif operator in ['+','-','*','/','**']:
            self.first_value = current_value
            self.operator = operator
            self.buttons_state('disabled')
            return 
        
        elif operator == '=' and self.operator:
            current_value = round(eval(self.first_value+self.operator+current_value) if self.operator else current_value,4)
            self.first_value = None
            self.operator = None
        
        self.display.insert(0, current_value)
        self.buttons_state()
    
    def buttons_state(self, state='normal'):
        '''change the state of the operateors'''
        if state == 'normal':
            for button in self.state_buttons[:-1]:
                button.config(state=state)
        
        elif state == 'disabled':
            for button in self.state_buttons[:-1]:
                button.config(state=state)
        
        if '.' not in self.display.get():
            self.state_buttons[-1].config(state='normal')
        else:
            self.state_buttons[-1].config(state='disabled')
    # end def buttons_state
        
    def run(self):
        self.make_layout()
        self.mainloop()

Calculator().run()
