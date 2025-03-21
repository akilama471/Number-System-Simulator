import tkinter as tk
from tkinter import filedialog, scrolledtext, ttk
import threading
import queue

def convert_number_system(input_value, from_base, to_base):
    try:
        # Convert the input value to an integer from the specified base
        number = int(input_value, from_base)
        if to_base == 2:
            return bin(number)[2:]  # Binary
        elif to_base == 8:
            return oct(number)[2:]  # Octal
        elif to_base == 10:
            return str(number)  # Decimal
        elif to_base == 16:
            return hex(number)[2:].upper()  # Hexadecimal
    except ValueError:
        return "Invalid input"

def view_file_as_binary(file_path, text_widget, progress_bar):
    file_queue = queue.Queue()

    def read_file():
        try:
            with open(file_path, 'rb') as file:
                file_size = file.seek(0, 2)  # Get file size
                file.seek(0)  # Reset file pointer to the beginning
                
                chunk_size = 1024
                bytes_read = 0
                
                while (chunk := file.read(chunk_size)):
                    bytes_read += len(chunk)
                    binary_data = ' '.join(format(byte, '08b') for byte in chunk)
                    file_queue.put(binary_data)
                    
                    progress = (bytes_read / file_size) * 100
                    file_queue.put(f"PROGRESS:{progress}")
                    
                file_queue.put("DONE")
        except Exception as e:
            file_queue.put(f"ERROR:{e}")

    def process_queue():
        try:
            while not file_queue.empty():
                data = file_queue.get()
                if data.startswith("PROGRESS:"):
                    progress = float(data.split(":")[1])
                    progress_bar['value'] = progress
                elif data == "DONE":
                    progress_bar['value'] = 100
                    break
                elif data.startswith("ERROR:"):
                    text_widget.insert(tk.END, data[6:] + '\n')
                    break
                else:
                    text_widget.insert(tk.END, data + '\n')
        except Exception as e:
            text_widget.insert(tk.END, f"Error processing queue: {e}\n")
        finally:
            if not file_queue.empty():
                text_widget.after(100, process_queue)

    threading.Thread(target=read_file, daemon=True).start()
    text_widget.after(100, process_queue)

def select_file_and_display_binary(text_widget, progress_bar):
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        text_widget.delete(1.0, tk.END)
        progress_bar['value'] = 0
        view_file_as_binary(file_path, text_widget, progress_bar)

def create_conversion_tab(tab):
    def perform_conversion():
        input_value = input_entry.get()
        from_base = int(from_base_combobox.get())
        to_base = int(to_base_combobox.get())
        result = convert_number_system(input_value, from_base, to_base)
        result_label.config(text=f"Result: {result}")

    tk.Label(tab, text="Enter Value:").grid(row=0, column=0, padx=10, pady=10)
    input_entry = tk.Entry(tab)
    input_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(tab, text="From Base:").grid(row=1, column=0, padx=10, pady=10)
    from_base_combobox = ttk.Combobox(tab, values=[2, 8, 10, 16], state="readonly")
    from_base_combobox.grid(row=1, column=1, padx=10, pady=10)
    from_base_combobox.set(10)

    tk.Label(tab, text="To Base:").grid(row=2, column=0, padx=10, pady=10)
    to_base_combobox = ttk.Combobox(tab, values=[2, 8, 10, 16], state="readonly")
    to_base_combobox.grid(row=2, column=1, padx=10, pady=10)
    to_base_combobox.set(2)

    convert_button = tk.Button(tab, text="Convert", command=perform_conversion)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)

    result_label = tk.Label(tab, text="Result:")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

def create_text_conversion_tab(tab):
    def perform_text_number_conversion():
        input_text = input_text_area.get("1.0", tk.END).strip()
        if not input_text:
            return

        binary_result = ' '.join(format(ord(char), '08b') for char in input_text)
        octal_result = ' '.join(format(ord(char), 'o') for char in input_text)
        decimal_result = ' '.join(str(ord(char)) for char in input_text)
        hexadecimal_result = ' '.join(format(ord(char), 'X') for char in input_text)

        binary_output_area.config(state=tk.NORMAL)
        binary_output_area.delete("1.0", tk.END)
        binary_output_area.insert(tk.END, binary_result)
        binary_output_area.config(state=tk.DISABLED)

        octal_output_area.config(state=tk.NORMAL)
        octal_output_area.delete("1.0", tk.END)
        octal_output_area.insert(tk.END, octal_result)
        octal_output_area.config(state=tk.DISABLED)

        decimal_output_area.config(state=tk.NORMAL)
        decimal_output_area.delete("1.0", tk.END)
        decimal_output_area.insert(tk.END, decimal_result)
        decimal_output_area.config(state=tk.DISABLED)

        hexadecimal_output_area.config(state=tk.NORMAL)
        hexadecimal_output_area.delete("1.0", tk.END)
        hexadecimal_output_area.insert(tk.END, hexadecimal_result)
        hexadecimal_output_area.config(state=tk.DISABLED)

    
    # Text Converter Tab
    input_label = ttk.Label(tab, text="Enter your text:")
    input_label.pack(anchor=tk.W, padx=10, pady=5)

    input_text_area = tk.Text(tab, wrap=tk.WORD, height=10)
    input_text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    convert_button = ttk.Button(tab, text="Convert", command=perform_text_number_conversion)
    convert_button.pack(pady=10)

    binary_label = ttk.Label(tab, text="Binary:")
    binary_label.pack(anchor=tk.W, padx=10, pady=5)

    binary_output_area = tk.Text(tab, wrap=tk.WORD, height=5, state=tk.DISABLED)
    binary_output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    octal_label = ttk.Label(tab, text="Octal:")
    octal_label.pack(anchor=tk.W, padx=10, pady=5)

    octal_output_area = tk.Text(tab, wrap=tk.WORD, height=5, state=tk.DISABLED)
    octal_output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    decimal_label = ttk.Label(tab, text="Decimal:")
    decimal_label.pack(anchor=tk.W, padx=10, pady=5)

    decimal_output_area = tk.Text(tab, wrap=tk.WORD, height=5, state=tk.DISABLED)
    decimal_output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    hexadecimal_label = ttk.Label(tab, text="Hexadecimal:")
    hexadecimal_label.pack(anchor=tk.W, padx=10, pady=5)

    hexadecimal_output_area = tk.Text(tab, wrap=tk.WORD, height=5, state=tk.DISABLED)
    hexadecimal_output_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

def create_gui():
    root = tk.Tk()
    root.title("Binary File Viewer and Number System Converter")
    root.geometry("800x600")

    # Create a tab control
    tab_control = ttk.Notebook(root)
    tab_control.pack(fill=tk.BOTH, expand=True)

    # Create tabs
    binary_viewer_tab = ttk.Frame(tab_control)
    conversion_tab = ttk.Frame(tab_control)
    text_conversion_tab = ttk.Frame(tab_control)

    tab_control.add(binary_viewer_tab, text="Binary Viewer")
    tab_control.add(conversion_tab, text="Number Converter")
    tab_control.add(text_conversion_tab, text="Text Converter")

    tab_control.pack(expand=1, fill="both")

    # Binary Viewer Tab
    select_file_button = tk.Button(binary_viewer_tab, text="Select File",
                                   command=lambda: select_file_and_display_binary(text_area, progress_bar))
    select_file_button.pack(pady=10)

    progress_bar = ttk.Progressbar(binary_viewer_tab, orient=tk.HORIZONTAL, length=400, mode='determinate')
    progress_bar.pack(pady=10)

    text_area = scrolledtext.ScrolledText(binary_viewer_tab, wrap=tk.WORD, width=100, height=30)
    text_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Conversion Tabs
    create_conversion_tab(conversion_tab)
    create_text_conversion_tab(text_conversion_tab)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
