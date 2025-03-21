import customtkinter

from binary_window import BinaryWindow

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x400")

        self.button_1 = customtkinter.CTkButton(self, text="Binary System", command=self.open_binary_window)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_binary_window(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = BinaryWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

app = App()
app.mainloop()