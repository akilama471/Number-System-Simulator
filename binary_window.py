import customtkinter

class BinaryWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("640x520")
        self.title("Binary Number System")

        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((1,2), weight=1)

        self.label1 = customtkinter.CTkLabel(self, text="ද්විමය සංඛ්‍යා පද්ධතිය - Binary Number System", 
                                             font=("Arial", 20), text_color="white")
        self.label1.grid(row=0, column=0, padx=20, pady=(20,20), sticky="ew", columnspan=2)

        self.symbols_frame = customtkinter.CTkFrame(self)
        self.symbols_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        self.symbols_frame.grid_columnconfigure(0, weight=1)  # Allow expansion

        self.base_frame = customtkinter.CTkFrame(self)
        self.base_frame.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="nsew")
        self.base_frame.grid_columnconfigure(0, weight=1)  # Allow expansion

        self.label2 = customtkinter.CTkLabel(self.symbols_frame, text="සංඛේත - Symbols", 
                                             font=("Arial", 20), text_color="white")
        self.label2.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")

        self.label3 = customtkinter.CTkLabel(self.base_frame, text="පාදය - Base", 
                                             font=("Arial", 20), text_color="white")
        self.label3.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="nsew")


# Run the window
if __name__ == "__main__":
    app = BinaryWindow()
    app.mainloop()
