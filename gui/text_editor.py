import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, colorchooser, font

# Function to open a file using the C executable
def open_file(event=None):
    file_path = filedialog.askopenfilename()
    if file_path:
        result = subprocess.run(['build/file_operations.exe', file_path], capture_output=True, text=True)
        if result.returncode != 0:
            messagebox.showerror("Error", "Failed to open file.")
            return
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, result.stdout)

# Function to save the file content
def save_file(event=None):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        content = text_area.get(1.0, tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Save File", "File saved successfully.")

# Function to find and replace text
def find_replace(event=None):
    find_text = simpledialog.askstring("Find", "Enter the text to find:")
    replace_text = simpledialog.askstring("Replace", "Enter the text to replace with:")
    if find_text and replace_text:
        content = text_area.get(1.0, tk.END)
        new_content = content.replace(find_text, replace_text)
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, new_content)
        messagebox.showinfo("Find & Replace", f"Replaced '{find_text}' with '{replace_text}'.")

# Function to copy selected text
def copy_text(event=None):
    text_area.event_generate("<<Copy>>")

# Function to cut selected text
def cut_text(event=None):
    text_area.event_generate("<<Cut>>")

# Function to paste text from clipboard
def paste_text(event=None):
    text_area.event_generate("<<Paste>>")

# Function to change font size
def change_font_size():
    size = simpledialog.askinteger("Font Size", "Enter the font size:")
    if size:
        current_font = font.nametofont(text_area['font'])
        current_font.configure(size=size)
        text_area.configure(font=current_font)

# Function to change font color
def change_font_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.configure(fg=color)

# Function to toggle between light and dark mode
def toggle_theme():
    global dark_mode
    if dark_mode:
        text_area.config(bg="white", fg="black", insertbackground="black")  # Light mode settings
        root.config(bg="white")
        dark_mode = False
    else:
        text_area.config(bg="#2E2E2E", fg="white", insertbackground="white")  # Dark mode settings
        root.config(bg="#2E2E2E")
        dark_mode = True

# Function to quit the application
def quit_app(event=None):
    root.quit()

# GUI setup
root = tk.Tk()
root.title("Enhanced Text Editor")
root.geometry("800x600")  # Set default window size to 800x600 pixels

# Set default mode (Light mode)
dark_mode = False

# Text area for editing files
text_area = tk.Text(root, wrap='word', undo=True, font=("Arial", 12), bg="white", fg="black", insertbackground="black")
text_area.pack(expand=1, fill='both')

# Adding a scroll bar
scrollbar = tk.Scrollbar(text_area)
scrollbar.pack(side='right', fill='y')
text_area.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_area.yview)

# Menu setup
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit_app, accelerator="Ctrl+Q")
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu for additional features
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Find & Replace", command=find_replace, accelerator="Ctrl+F")
edit_menu.add_separator()
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Format menu for font customization
format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font Size", command=change_font_size)
format_menu.add_command(label="Font Color", command=change_font_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

# View menu for toggling themes
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Toggle Dark/Light Mode", command=toggle_theme)
menu_bar.add_cascade(label="View", menu=view_menu)

root.config(menu=menu_bar)

# Binding keyboard shortcuts
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_file)
root.bind('<Control-f>', find_replace)
root.bind('<Control-q>', quit_app)
root.bind('<Control-c>', copy_text)
root.bind('<Control-x>', cut_text)
root.bind('<Control-v>', paste_text)

root.mainloop()
