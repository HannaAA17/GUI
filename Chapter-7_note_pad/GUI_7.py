import tkinter
import tkinter.scrolledtext
import tkinter.messagebox
import tkinter.filedialog

from PIL import Image, ImageTk

# // cSpell:ignore endregion

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

        # region Create Frames
        menu_frame = tkinter.Frame(self, bg=menu_color)
        menu_frame.pack(padx=5, pady=5)

        text_frame = tkinter.Frame(self, bg=text_color)
        text_frame.pack(padx=5, pady=5)
        # endregion Create Frames

        # region Define Functions
        def open_note():
            """Open a previously saved note.  First three lines of note are font family, font size, and font option.  First set the font, then load the text."""
            
            # Use filedialog to get location and directory of note file
            open_name = tkinter.filedialog.askopenfilename(
                initialdir="./", title='Open Note',
                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
            )
            
            if not open_name: return
            
            with open(open_name, 'r') as f:
                #Clear the current text
                input_text.delete("1.0", tkinter.END)

                # First three lines are font_family, font_size, and font_option
                font_family.set(f.readline().strip())
                font_size.set(int(f.readline().strip()))
                font_option.set(f.readline().strip())

                # Call the change font for these .set() and pass an arbitrary value
                change_font(1)

                # Read the rest of the file and insert it into the text field
                text = f.read()
                input_text.insert("1.0", text)
        # end def open_note
        
        def new_note():
            """Create a new Note which essentially clears the screen."""
            
            # Use a messagebox to ask for a new note
            question = tkinter.messagebox.askyesno(
                "New Note", "Are you sure you want to start a new note?"
            )
            
            if question == 1:
                # ScrolledText widgets starting index is 1.0 not 0.
                input_text.delete("1.0", tkinter.END)
        # end def new_note
        
        def close_note():
            """Closes the note which essentially quits the program."""
            
            # Use a messagebox to ask to close
            question = tkinter.messagebox.askyesno(
                "Close Note", "Are you sure you want to close your note?"
            )
            
            if question == 1:
                self.destroy()
        # end def close_note
        
        def save_note():
            """Save the given note.  First three lines are saved as font family, font size, and font option."""
            
            # Use filedialog to get location and name of where/what to save the file as.
            save_name = tkinter.filedialog.asksaveasfilename(
                initialdir="./", title="Save Note",
                filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
            )
            
            if not save_name:
                return
            
            elif not save_name.endswith('.txt'):
                save_name += '.txt'
            
            with open(save_name, 'w') as f:
                # First three lines of save file are font_family, font_size, and font_options.Font_size must be a string not int.
                f.write(font_family.get() + "\n")
                f.write(str(font_size.get()) + "\n")
                f.write(font_option.get() + "\n")

                # write remaining text in field to the file
                f.write(input_text.get("1.0", tkinter.END))
        # end def save_note
        
        def change_font(event):
            """Change the given font based off dropbox options."""
            if font_option.get() == 'none':
                my_font = (font_family.get(), font_size.get())
            else:
                my_font = (font_family.get(), font_size.get(), font_option.get())

            # Change the font style
            input_text.config(font=my_font)
        # end def change_font
        # endregion Define Functions

        # region Create the menu: new, open, save, close buttons
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
        self.images = {
            'new_image': new_image, 'open_image': open_image,
            'save_image': save_image, 'close_image': close_image,
        }
        # endregion Create the menu: new, open, save, close buttons

        # region Create the menu: font family, font size, font option dropdown-lists
        families = [
            'Arial', 'Calibri', 'Cambria', 'Courier', 'Georgia', 'MS Gothic',
            'Modern', 'Script', 'SimSun', 'Tahoma', 'Terminal', 'Times New Roman',
            'Verdana', 'Wingdings'
        ]
        # from tkinter.font import families; print(sorted(families()))
        font_family = tkinter.StringVar(value='Arial')
        font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
        font_family_drop.config(width=len(max(families, key=len)))
        font_family_drop.grid(row=0, column=4, padx=5, pady=5)

        sizes = range(8, 68, 4)
        font_size = tkinter.IntVar(value=8)
        font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
        font_size_drop.config(width=2)
        font_size_drop.grid(row=0, column=5, padx=5, pady=5)

        options = ['none', 'bold', 'italic']
        font_option = tkinter.StringVar(value='none')
        font_option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
        font_option_drop.config(width=len(max(options, key=len)))
        font_option_drop.grid(row=0, column=6, padx=5, pady=5)
        # endregion Create the menu: font family, font size, font option

        # region Create the ScrolledText widget
        my_font = (font_family.get(), font_size.get())

        input_text = tkinter.scrolledtext.ScrolledText(
            text_frame, width=1000, height=100, bg=text_color, font=my_font
        )
        
        input_text.pack()
        # endregion Create the ScrolledText widget

        ...
    # end def define_layout

    def run(self):
        self.define_layout()
        self.mainloop()
# end class Notepad

Notepad().run()