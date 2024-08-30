# Enhanced Text Editor

This is an enhanced text editor built using Python for the GUI and C for file handling operations. The editor includes features like find & replace, copy, cut, paste, dark/light mode toggle, and keyboard shortcuts for a seamless editing experience.

## Features

- **Basic File Operations**: Open, Save files using C executable.
- **Editing Functions**: Copy, Cut, Paste.
- **Find & Replace**: Search and replace text easily.
- **Dark/Light Mode Toggle**: Switch between themes.
- **Keyboard Shortcuts**: Save (`Ctrl+S`), Open (`Ctrl+O`), Quit (`Ctrl+Q`), and more.
- **Resizable and User-Friendly GUI**: Comes with scrollbars and adjustable window size.

## Getting Started

### Prerequisites

- Python 3.x
- GCC compiler (for compiling C code)
- Tkinter (usually included with Python)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Enhanced-Text-Editor.git
   cd Enhanced-Text-Editor
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Compile the C code:

   ```bash
   gcc core/file_operations.c -o build/file_operations
   ```

4. Run the Python GUI:

   ```bash
   python gui/text_editor.py
   ```

## Usage

- **Open File**: `Ctrl+O` or use the File menu.
- **Save File**: `Ctrl+S` or use the File menu.
- **Toggle Dark/Light Mode**: Use the View menu.
- **Find & Replace**: `Ctrl+F` or use the Edit menu.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
