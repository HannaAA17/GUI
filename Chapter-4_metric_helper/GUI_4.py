import tkinter
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

# region chapter2

'''lesson1: title, icon, geometry, resizable, config, Toplevel'''
class lesson1:
    def __init__(self) -> None:
        # Define window
        root = tkinter.Tk()
        # rename window
        root.title('Window Basics')
        # change logo
        root.iconbitmap('thinking.ico')
        # change size
        root.geometry('250x250')
        # resizable x,y
        root.resizable(0, 1)
        # back ground color
        root.config(bg='blue')

        self.root = root
    # end def __init__

    def add_second_window(self):
        # second window
        top = tkinter.Toplevel()
        top.title('Window Basics')
        top.config(bg='#123456')
        # offset 500 in x and 50 in -y
        top.geometry('250x250+500+50')

        self.top = top
    # end def add_second_window

    def run(self):
        # Run the main loop
        self.add_second_window()
        self.root.mainloop()
# lesson1().run()

'''lesson2: Labels, pack'''
class lesson2:
    def __init__(self):
        # Define window
        root = tkinter.Tk()
        root.title('Label Basics!')
        root.iconbitmap('thinking.ico')
        root.geometry('400x400')
        root.resizable(0, 0)
        root.config(bg='blue')

        self.root = root
    # end def __init__

    def create_widgets(self):
        root = self.root

        # making label
        name_label_1 = tkinter.Label(
            root,
            text='Hello, my name is Dodo.'
        )
        name_label_1.pack()

        # Add font formating
        name_label_2 = tkinter.Label(
            root,
            text='Hello, my name is Dodo2.',
            font=('Arial', 18, 'bold')
        )
        name_label_2.pack()

        # Using config, external padding
        name_label_3 = tkinter.Label(root)
        name_label_3.config(
            text='Hello, my name is Dodo3.',
            font=('Cambria', 10),
            bg='#ff0000'  # red
        )
        name_label_3.pack(
            padx=10,
            pady=50
        )

        # customizing external panding
        # adding internal panding
        # anchoring
        name_label_4 = tkinter.Label(
            root,
            text='Hello, my name is Dodo4.',
            fg='green',  # font color
            bg='#000000',  # back ground, black
        )
        name_label_4.pack(
            pady=(0, 10),  # 0 above, 10 below
            ipadx=50,
            ipady=10,
            anchor='w',
        )

        # fill
        name_label_5 = tkinter.Label(
            root,
            text='Hello, my name is Dodo5.',
            fg='#123456',  # font color
            bg='#ffffff',  # background, white
        )
        name_label_5.pack(
            # fill='y', # fill for the hight of the caption
            fill='both',
            expand=True,  # expand to take all the free space
            padx=10,
            pady=10,
        )

        self.root = root
    # end def create_widgets

    def run(self):
        # Run the main loop
        self.create_widgets()
        self.root.mainloop()
# lesson2().run()

'''lesson3: button, grid'''
class lesson3(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Button Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('500x500')
        self.resizable(0, 0)
    # end def __init__

    def create_buttons(self):
        # create button
        self.name_button = tkinter.Button(self, text='Name')
        # make grid
        self.name_button.grid(row=0, column=0)

        self.time_button = tkinter.Button(self, text='Time', bg='#00ffff')
        self.time_button.grid(row=0, column=1)

        # activebackground
        self.place_button = tkinter.Button(self, text='Place', bg='#00ffff', activebackground='#ff0000')
        self.place_button.grid(row=0, column=2, padx=10, pady=10, ipadx=15)

        # borderwidth, columnspan (take all the space), sticky(location on the cell)
        self.day_button = tkinter.Button(self, text='Day', bg='black', fg='white', borderwidth=5)
        self.day_button.grid(row=1, column=0, columnspan=3, sticky='WE')

        # collection
        self.test1 = tkinter.Button(self, text='test1')
        self.test2 = tkinter.Button(self, text='test2')
        self.test3 = tkinter.Button(self, text='test3')
        self.test4 = tkinter.Button(self, text='test4')
        self.test5 = tkinter.Button(self, text='test5')
        self.test6 = tkinter.Button(self, text='test6')
        
        self.test1.grid(row=2, column=0, padx=5, pady=5)
        self.test2.grid(row=2, column=1, padx=5, pady=5)
        self.test3.grid(row=2, column=2, padx=5, pady=5, sticky='W')
        self.test4.grid(row=3, column=0, padx=5, pady=5)
        self.test5.grid(row=3, column=1, padx=5, pady=5)
        self.test6.grid(row=3, column=2, padx=5, pady=5, sticky='W')
    # end def create_buttons

    def run(self):
        self.create_buttons()
        self.mainloop()
# lesson3().run()

'''lesson4: Frames'''
class lesson4(tkinter.Tk) :
    def __init__(self):
        super().__init__()
        self.title('Frame Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('500x500')
        self.resizable(0, 0)
    # end def __init__

    def create_frames(self):
        self.pack_frame = tkinter.Frame(self, bg='red')
        self.grid_frame1 = tkinter.Frame(self, bg='blue')
        self.grid_frame2 = tkinter.LabelFrame(self, text='Grid system rules!')

        self.pack_frame.pack(fill='both', expand=True)
        self.grid_frame1.pack(fill='x', expand=True)
        self.grid_frame2.pack(fill='both', padx=10, pady=10, expand=True)

        tkinter.Label(self.pack_frame, text='text').pack()
        tkinter.Label(self.pack_frame, text='text').pack()
        tkinter.Label(self.pack_frame, text='text').pack()
        
        tkinter.Label(self.grid_frame1, text='text').grid(row=0, column=0)
        tkinter.Label(self.grid_frame1, text='text').grid(row=1, column=1)
        tkinter.Label(self.grid_frame1, text='text').grid(row=2, column=2)
    # end def create_frames

    def run(self):
        self.create_frames()
        self.mainloop()
# lesson4().run()

'''lesson5: Functions'''
class lesson5(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Entry Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('500x500')
        self.resizable(0, 0)
    # end def __init__
    
    def create_button(self):
        # define frames
        input_frame = tkinter.Frame(self, bg='#0000ff', width=500, height=100)
        output_frame = tkinter.Frame(self, bg='#ff0000', width=500, height=400)
        
        input_frame.pack(padx=10, pady=10)
        output_frame.pack(padx=10, pady=(0,10))
        
        # add entry
        text_entry = tkinter.Entry(input_frame, width=50)
        text_entry.grid(row=0, column=0, padx=5, pady=5)
        text_entry.bind('<Return>', self.make_label)
        
        
        # the frame has taken the shape of the widget that it holds
        input_frame.grid_propagate(0)
        output_frame.pack_propagate(0)
        
        # make print button 
        print_button = tkinter.Button(input_frame, text='Print!', command=self.make_label)
        print_button.grid(row=0, column=1, padx=5, pady=5, ipadx=30)

        # make count button
        self.value = 0
        count_button = tkinter.Button(
            input_frame, text='Count!',
            command= lambda : self.count_up(self.value)
        )
        count_button.grid(
            row=1, column=0, padx=5, pady=5,
            columnspan=2, sticky="WE" # stritch the button
        )
        
        # add to the self
        self.text_entry = text_entry
        self.output_frame = output_frame   
    # end def create_button
    
    def make_label(self, *kwards):
        '''print a label'''
        txt = self.text_entry.get() or 'Blank!'
        self.text_entry.delete(0, tkinter.END)
        
        text = tkinter.Label(self.output_frame, text=txt, bg='#ff0000')
        text.pack()
    # end def make_label
        
    def count_up(self, value):
        '''print a count'''
        text = tkinter.Label(self.output_frame, text=value, bg='#ff0000')
        text.pack()
        
        self.value += 1
    # end def count_up
    
    def run(self):
        self.create_button()
        self.mainloop()
# lesson5().run()

'''lesson6: Radio Buttons'''
class lesson6(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Entry Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('350x350')
        self.resizable(0, 0)
    # end def __init__
    
    def define_widgets(self):
        # define frames
        input_frame = tkinter.LabelFrame(self, text='This is fun', width=350, height=100)
        output_frame = tkinter.Frame(self, width=350, height=250)
        
        input_frame.pack(padx=10, pady=10)
        output_frame.pack(padx=10, pady=(0,10))
        
        # Define variables
        self.number = tkinter.IntVar()
        
        self.number.set(1) # select the first radio
        
        # define radio buttons
        radio_1 = tkinter.Radiobutton(input_frame, text='Print the number one!', variable=self.number, value=1)
        radio_2 = tkinter.Radiobutton(input_frame, text='Print the number two!', variable=self.number, value=2)
        print_button = tkinter.Button(input_frame, text='Print the number!', command=self.make_label)
        
        radio_1.grid(row=0, column=0, padx=10, pady=10)
        radio_2.grid(row=0, column=1, padx=10, pady=10)
        print_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        self.output_frame = output_frame

    # end def define_widgets
    
    def make_label(self):
        '''print to screen'''
        num_label = tkinter.Label(
            self.output_frame, 
            text=["1 one 1", "2 two 2"][self.number.get()-1]
        )
        
        num_label.pack()
    
    def run(self):
        self.define_widgets()
        self.mainloop()
# lesson6().run()

'''lesson7: images'''
class lesson7(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Image Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('700x700')
        self.resizable(1, 1)
    # end def __init__
    
    def add_image(self):
        # Images must be global or added to the self if used in functions
        self.my_image = tkinter.PhotoImage(file='shield.png')
        
        my_label = tkinter.Label(self, image=self.my_image)
        my_label.pack()
        
        my_button = tkinter.Button(self, image=self.my_image)
        my_button.pack()
        
        # using jpg images
        self.cat_image = ImageTk.PhotoImage(Image.open('cat.jpg'))
        cat_label = tkinter.Label(self, image=self.cat_image)
        cat_label.pack()
    # end add_image
    def run(self):
        self.add_image()
        self.mainloop()
# lesson7().run()

# endregion chapter2

# region chapter3

'''Hello GUI World'''
class C3lesson1(tkinter.Tk):
    # define shape, fonts and colors
    def __init__(self):
        super().__init__()
        self.title('Hello GUI World!')
        self.iconbitmap('wave.ico')
        self.geometry('400x400')
        self.resizable(0, 0)
        
        # https://coolors.co/
        self.root_color = '#224870'
        self.input_color = '#2a4494'
        self.output_color = '#4ea5d9'
        
        # apply color
        self.config(bg=self.root_color)
    # end def __init__

    # Define layout
    def create_widgets(self):
        # create frames
        input_frame = tkinter.LabelFrame(self, bg=self.input_color)
        output_frame = tkinter.LabelFrame(self, bg=self.output_color)
        
        input_frame.pack(pady=10)
        output_frame.pack(padx=10, pady=(0,10), fill='both', expand=True)
        
        # create widgets
        name_ent = tkinter.Entry(input_frame, text='Enter your name', width=20)
        submit_button = tkinter.Button(input_frame, text='Submit', command=self.submit_name)
        name_ent.bind('<Return>', self.submit_name)
        
        name_ent.grid(row=0, column=0, padx=10, pady=10)
        submit_button.grid(row=0, column=1, padx=10, pady=10, ipadx=20)
    
        # create radio buttons
        ## create variable
        self.case_style = tkinter.IntVar()
        self.case_style.set(0)
        
        ## create buttons
        normal_button = tkinter.Radiobutton(
            input_frame, text='Normal Case', variable=self.case_style, value=0,
            bg=self.input_color, activebackground=self.input_color
        )
        upper_button = tkinter.Radiobutton(
            input_frame, text='Upper Case', variable=self.case_style, value=1,
            bg=self.input_color, activebackground=self.input_color
        )
        
        normal_button.grid(row=1, column=0, padx=2, pady=2)
        upper_button.grid(row=1, column=1, padx=2, pady=2)
        
        # add image
        self.smile_img = ImageTk.PhotoImage(Image.open('smile.png'))
        smile_label = tkinter.Label(output_frame, image=self.smile_img, bg=self.output_color)
        smile_label.pack()
        
        # add to self
        self.output_frame = output_frame
        self.name_ent = name_ent
    # end def create_widgets
    
    # Define functions
    def submit_name(self, e=''):
        txt = [lambda x:x, lambda x: x.upper()][self.case_style.get()]
        name_label = tkinter.Label(
            self.output_frame, text=txt(f'Hello {self.name_ent.get()}! Keep Learning Tkinter'),
            bg=self.output_color
        )
        name_label.pack()
        
        self.name_ent.delete(0, tkinter.END)
    # end def submit_name
    
    def run(self):
        self.create_widgets()
        self.mainloop()
# C3lesson1().run()

# endregion chapter3

# region chapter4

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
        self.input_field = tkinter.Entry(self, width=20, font=self.field_font, borderwidth=3)
        equal_label = tkinter.Label(self, text='=', font=self.field_font, bg=self.bg_color)
        self.output_field = tkinter.Entry(self, width=20, font=self.field_font, borderwidth=3)
        to_label = tkinter.Label(self, text='to', font=self.field_font, bg=self.bg_color)
        convert_button = tkinter.Button(self, text='Convert',command=self.calculate, font=self.field_font, bg=self.button_color)
        
        # place widgets
        self.input_field.grid(row=0, column=0, padx=10, pady=10)
        equal_label.grid(row=0, column=1, padx=10, pady=10)
        self.output_field.grid(row=0, column=2, padx=10, pady=10)
        to_label.grid(row=1, column=1, padx=10, pady=10)
        convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)

        # add place holder
        self.input_field.insert(0, 'Enter your quantity:')
    # end def create_widgets
    
    def create_option_menu(self):
        # define control variables
        self.input_choice = tkinter.StringVar()
        self.output_choice = tkinter.StringVar()
        
        input_dropdown = tkinter.OptionMenu(self, self.input_choice, *self.metric_list_n)
        output_dropdown = tkinter.OptionMenu(self, self.output_choice, *self.metric_list_n)
        
        input_dropdown.grid(row=1, column=0)
        output_dropdown.grid(row=1, column=2)
        
        self.input_choice.set('base value')
        self.output_choice.set('base value')
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
    def calculate(self):
        try:
            cal = lambda x: 10**self.metric_list_v[self.metric_list_n.index(x)]
            
            from_v = float(self.input_field.get()) * cal(self.input_combobox.get())
            to_v = from_v / cal(self.output_combobox.get())
            
            self.output_field.delete(0, tkinter.END)
            self.output_field.insert(0, str(to_v))
        except:
            messagebox.showerror("Invalid Input!", "Please Enter a Valid Number")
    # end def calculate
      
    def run(self):
        self.create_widgets()
        # self.create_option_menu()
        self.create_combobox()
        self.mainloop()
c4lesson().run()

# endregion chapter4


'''lesson: '''
class lesson(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Entry Basics!')
        self.iconbitmap('thinking.ico')
        self.geometry('500x500')
        self.resizable(0, 0)
    # end def __init__

    def run(self):
        # self.create_button()
        self.mainloop()
# lesson().run()