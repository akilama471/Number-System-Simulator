import tkinter as tk
from tkinter import PanedWindow, filedialog, scrolledtext, ttk

def create_gui():
    # Initialize the main Tkinter window
    root = tk.Tk()
    root.title("Binary File Viewer and Number System Converter")
    root.geometry("800x600")
    root.resizable(False, False)

    # Create the main panel as a PanedWindow
    main_panel = PanedWindow(root)
    main_panel.pack(fill=tk.BOTH, expand=1)

    # Left panel with green background
    left_panel = tk.Frame(main_panel, bg="green", width=600)
    main_panel.add(left_panel)
    main_panel.paneconfigure(left_panel, minsize=600)  # Set minimum width for the left panel

    # Create the second panel with a red background
    right_panel = tk.Frame(main_panel, bg="red", width=200)
    main_panel.add(right_panel)
    main_panel.paneconfigure(right_panel, minsize=200)

    # Select file button on the left panel
    select_file_button = tk.Button(left_panel, text="Select File")
    select_file_button.pack(pady=10)

    # Progress bar on the left panel
    progress_bar = ttk.Progressbar(left_panel, orient=tk.HORIZONTAL, length=400, mode='determinate')
    progress_bar.pack(pady=10)

    # Text area for file contents on the left panel
    text_area = scrolledtext.ScrolledText(left_panel, wrap=tk.WORD, width=100, height=30)
    text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
