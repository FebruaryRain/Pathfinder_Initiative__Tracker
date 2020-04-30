from tkinter import Tk, Button, Label, Entry
import character_class

class windows:

    def __init__(self, window):
        self.generate_main_window(window)
        return  

    def generate_main_window(self, window):
        self.root = window
        root.title("Pathfinder Initiative Tracker")
        self.char_input_button = Button(text = "Input Character")
        self.char_input_button.grid(row = 0, column = 0)
        self.char_input_button.bind('<Button-1>', self.create_char_handler)
        root.mainloop()
        return

    def create_char_handler(self, event):
        char_creation_window = Tk()
        new_character_window(char_creation_window)
        return


class new_character_window:

    new_char_name = "Barry"

    def __init__(self, input_window):
        self.generate_character_input_window(input_window)
        return

    def generate_character_input_window(self, input_window):
        global new_char_name
        #input_window = Tk()
        input_window.title("Character Input")

        Label(input_window, text = "Character Name").grid(row = 0, column = 0)
        self.character_name = Entry(input_window)
        self.character_name.focus_set()
        self.character_name.insert(10, "Erwin")
        self.character_name.grid(row = 0, column = 1)

        confirm = Button(input_window, text = "Confirm")
        confirm.grid(row = 1)
        confirm.bind('<Button-1>', self.confirm_character_handler)

        input_window.mainloop()
        return

    def confirm_character_handler(self, event):
        print("Char confirmed")
        self.set_new_char_name(self.get_new_char_name)
        print("Name is", self.get_new_char_name())
        return

    def get_new_char_name(self):
        return self.character_name.get()

    def set_new_char_name(self, new_name):
        global new_char_name
        new_char_name = new_name
        return

if __name__ == "__main__":
    root = Tk()
    window = windows(root)
    #window.generate_main_window()
    #root.mainloop()
