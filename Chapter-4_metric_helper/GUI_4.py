import tkinter
from tkinter import ttk, messagebox
from PIL import ImageTk, Image


'''Metric Helper'''
class c4lesson(tkinter.Tk):
    def __init__(self):
        super().__init__()
        
        self.title('Metric Helper!')
        self.iconbitmap('ruler.ico')
        # self.geometry('500x500')
        self.resizable(0, 0)
        
        # define fonts
        self.field_font = ('Cambria', 10)
        
        # define colors
        ## https://imagecolorpicker.com/en
        self.bg_color = '#c75c5c'
        self.button_color = '#f5cf87'
        
        self.config(bg=self.bg_color)
        
        # define variables
        self.metric_list_n = ['yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'base value', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto'][-1::-1]
        self.metric_list_v = [24, 21, 18, 15, 12, 9, 6, 3, 2, 1, 0, -1, -2, -3, -6, -9, -12, -15, -18, -21, -24][-1::-1]
    # end def __init__
    
    def create_widgets(self):
        # define widgets
        input_field = tkinter.Entry(self, width=20, font=self.field_font, borderwidth=3)
        equal_label = tkinter.Label(self, text='=', font=self.field_font, bg=self.bg_color)
        output_field = tkinter.Entry(self, width=20, font=self.field_font, borderwidth=3)
        to_label = tkinter.Label(self, text='to', font=self.field_font, bg=self.bg_color)
        convert_button = tkinter.Button(self, text='Convert',command=self.calculate, font=self.field_font, bg=self.button_color)
        
        # place widgets
        input_field.grid(row=0, column=0, padx=10, pady=10)
        equal_label.grid(row=0, column=1, padx=10, pady=10)
        output_field.grid(row=0, column=2, padx=10, pady=10)
        to_label.grid(row=1, column=1, padx=10, pady=10)
        convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

        # add place holder
        input_field.insert(0, 'Enter your quantity:')
        
        # save in self
        self.input_field = input_field
        self.output_field = output_field
    # end def create_widgets
    
    def create_option_menu(self):
        # define control variables
        input_choice = tkinter.StringVar()
        output_choice = tkinter.StringVar()
        
        input_dropdown = tkinter.OptionMenu(self, input_choice, *self.metric_list_n)
        output_dropdown = tkinter.OptionMenu(self, output_choice, *self.metric_list_n)
        
        input_dropdown.grid(row=1, column=0)
        output_dropdown.grid(row=1, column=2)
        
        input_choice.set('base value')
        output_choice.set('base value')
        
        # save to self
        self.input_choice = input_choice
        self.output_choice = output_choice
    # end def create_option_menu
    
    def create_combobox(self):
        self.input_combobox = ttk.Combobox(self, font=self.field_font, justify='center', value=self.metric_list_n)
        self.output_combobox = ttk.Combobox(self, font=self.field_font, justify='center', value=self.metric_list_n)
        
        self.input_combobox.grid(row=1, column=0, padx=10, pady=10)
        self.output_combobox.grid(row=1, column=2, padx=10, pady=10)
        
        self.input_combobox.set('base value')
        self.output_combobox.set('base value')
    # end def create_combobox
    
    # Define functions
    def __wrap_exception(func):
        """This decorator wraps function to handle exceptions."""
        def _func_wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except:
                 messagebox.showerror("Invalid Input!", "Please Enter a Valid Number")
        
        return _func_wrapper

    @__wrap_exception
    def calculate(self):

        cal = lambda x: 10**self.metric_list_v[self.metric_list_n.index(x)]
        
        from_v = float(self.input_field.get()) * cal(self.input_combobox.get())
        to_v = from_v / cal(self.output_combobox.get())
        
        self.output_field.delete(0, tkinter.END)
        self.output_field.insert(0, str(to_v))
    # end def calculate
      
    def run(self):
        self.create_widgets()
        # self.create_option_menu()
        self.create_combobox()
        self.mainloop()
c4lesson().run()
