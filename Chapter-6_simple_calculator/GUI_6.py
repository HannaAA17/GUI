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
