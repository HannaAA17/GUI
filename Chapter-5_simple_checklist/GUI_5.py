import tkinter

'''lesson: '''
class clesson(tkinter.Tk):
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


# region chapter5

'''Simple Checklist'''
class c5lesson(tkinter.Tk):
    def __init__(self):
        # root
        super().__init__()
        
        # window layout
        self.title('Simple Checklist')
        self.iconbitmap('check.ico')
        self.geometry('400x400')
        self.resizable(0, 0)
        
        # fonts and colors
        self.my_font = ('Times New Roman', 12)
        self.root_color = '#6c1cbc'
        self.button_color = '#e2cff4'
        self.config(bg=self.root_color)
        
    # end def __init__
    
    def create_frames(self):
        # define frames
        input_frame = tkinter.Frame(self, bg=self.root_color)
        output_frame = tkinter.Frame(self, bg=self.root_color)
        button_frame = tkinter.Frame(self, bg=self.root_color)
        
        input_frame.pack()
        output_frame.pack()
        button_frame.pack()
        
        # input frame layout
        list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=self.my_font)
        list_entry.bind('<Return>', self.add_item)
        list_add_button = tkinter.Button(input_frame, command=self.add_item, text='Add Item', borderwidth=2, bg=self.button_color, font=self.my_font)
        
        list_entry.grid(row=0, column=0, padx=5, pady=5)
        list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)
        
        # output frame layout
        my_listbox = tkinter.Listbox(output_frame, height=15, width=45, borderwidth=3, font=self.my_font)
        my_listbox.grid(row=0, column=0)

        # buttons
        list_remove_button = tkinter.Button(button_frame, command=self.remove_item, text='Remove Item', borderwidth=2, bg=self.button_color, font=self.my_font)
        list_Clear_button = tkinter.Button(button_frame,command=self.clear_list, text='Clear List', borderwidth=2, bg=self.button_color, font=self.my_font)
        Save_button = tkinter.Button(button_frame, command=self.save_list, text='Save List', borderwidth=2, bg=self.button_color, font=self.my_font)
        quit_button = tkinter.Button(button_frame, text='Quit', borderwidth=2, bg=self.button_color, font=self.my_font, command=self.destroy)
        
        list_remove_button.grid(row=0,column=1, padx=2, pady=10) # big enough
        list_Clear_button.grid(row=0,column=2, padx=2, pady=10, ipadx=10)
        Save_button.grid(row=0,column=3, padx=2, pady=10, ipadx=10)
        quit_button.grid(row=0,column=4, padx=2, pady=10, ipadx=24)

        # add scroll bar
        my_scrollbar = tkinter.Scrollbar(output_frame)
        my_scrollbar.grid(row=0, column=1, sticky='NS')
        
        # link the scroll bar, link the scroll bar size
        my_scrollbar.config(command=my_listbox.yview)
        my_listbox.config(yscrollcommand=my_scrollbar.set)
        
        # save to self
        self.my_listbox = my_listbox
        self.list_entry = list_entry
    # end def create_frames
    
    def __wrap_exception(func):
        """This decorator wraps function to handle exceptions."""
        def _func_wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except:
                # messagebox.showerror("Invalid Input!", "Please Enter a Valid Number")
                pass
        return _func_wrapper
    
    def add_item(self, e=''):
        '''add item to the listbox'''
        if self.list_entry.get():
            self.my_listbox.insert(tkinter.END, self.list_entry.get())
        
        self.list_entry.delete(0, tkinter.END)
    
    def remove_item(self):
        '''remove the selected item from the listbox'''
        self.my_listbox.delete(tkinter.ANCHOR)
    
    def clear_list(self):
        '''delete all items from the list'''
        self.my_listbox.delete(0, tkinter.END)
    
    def save_list(self):
        '''save list to simple txt'''
        with open('list.txt','w') as f:
            for item in self.my_listbox.get(0, tkinter.END):
                f.write(item + '\n')
    
    @__wrap_exception
    def open_list(self):
        '''open the list upon starting'''
        with open('list.txt','r') as f:
            for line in f:
                self.my_listbox.insert(tkinter.END, line.strip())
    
    def run(self):
        self.create_frames()
        self.open_list()
        self.mainloop()
c5lesson().run()

# end region chapter5