import tkinter
from PIL import ImageTk, Image

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
C3lesson1().run()
