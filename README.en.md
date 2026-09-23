# 📋 Clipboard History Manager

<p align="center">
  <a href="README.md">Português</a> | <b>English</b> | <a href="README.es.md">Español</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/GUI-Tkinter%20%7C%20ttkbootstrap-darkgreen" alt="GUI Framework" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white" alt="Platform" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
</p>

A modern, fast, and lightweight clipboard history manager for **Windows**, built with **Python**, **Tkinter**, and **ttkbootstrap**.

Automatically track everything you copy (texts, URLs, and images), organize by tabs with a refined design, edit items on the fly, and customize themes and languages with real-time hot-reloading.

---

## ✨ Key Features

- 🔄 **Continuous Clipboard Monitoring**: Automatically captures copied texts, web links, and screenshots without interrupting your workflow.
- 🗂️ **Smart Tab Categorization**:
  - **Texts**: History of regular copied texts.
  - **Links**: Automatic detection and separation of web URLs (`http://` and `https://`).
  - **Images**: History with thumbnails, timestamps, and image hashes.
- 🎨 **Modern & Polished Interface**:
  - Custom Canvas components (`RoundedButton`, `CustomTabBar`, `CustomList`) with rounded corners, subtle hover feedback, and pill-shaped active selection.
  - Minimalist scrollbars matching the color palette.
  - Full support for **Dark Mode** and **Light Mode**.
  - 4 Accent Colors: **Purple**, **Teal**, **Blue**, and **Red**.
- 🌐 **Multi-Language Support (i18n)**:
  - 🇧🇷 Português (Brasil)
  - 🇺🇸 English
  - 🇪🇸 Español
- ⚡ **Real-Time Hot-Reload**: Change themes, accent colors, or languages and see the entire interface update instantly, **with no restart required**.
- 🖼️ **4 Image View Modes**:
  - Details (List with timestamp and file hash)
  - Small Icons (64x64)
  - Medium Icons (128x128)
  - Large Icons (256x256)
- ✏️ **Built-in Quick Editor**: Floating window to inspect and edit text entries on the fly.
- 💾 **Quick TXT Export**: Save any selected text or link directly to a `.txt` file.
- 🗑️ **Recycle Bin (Deleted Items)**: Safely remove entries with restore or permanent deletion options.

---

## 🛠️ Built With

- **[Python 3.12](https://www.python.org/)** — Core programming language.
- **Tkinter** — Built-in Python GUI framework.
- **[ttkbootstrap](https://ttkbootstrap.readthedocs.io/)** — Modern theme styling and ttk widgets.
- **[Pillow (PIL)](https://python-pillow.org/)** — Clipboard image grab, manipulation, and rendering.
- **[PyInstaller](https://pyinstaller.org/)** — Packaging into a standalone Windows executable.

---

## 📂 Project Structure

```plaintext
Clipboard History/
│
├── .gitignore             # Git ignore rules
├── clipboard_history.py   # Main application source code
├── requirements.txt       # Project dependencies
├── README.md              # Portuguese documentation
├── README.en.md           # English documentation (current)
└── README.es.md           # Spanish documentation
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.10 or higher** installed on your system.

### 1. Clone the repository

```bash
git clone https://github.com/RickHardBR/Clipboard-History.git
cd Clipboard-History
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python clipboard_history.py
```

---

## 📦 Building the Executable (.exe)

You can package the program into a single standalone Windows executable that runs without requiring a Python installation:

Run the following command in the project root:

```powershell
pyinstaller --onefile --windowed --name "ClipboardHistory" clipboard_history.py
```

The output binary will be located at:
```
dist/ClipboardHistory.exe
```

> **Note:** The `--windowed` flag ensures the application runs cleanly as a desktop GUI without spawning a terminal/console window.

---

## ⚙️ Configuration & Preferences

Preferences are automatically stored in the `config.json` file in the project root:

```json
{
    "theme": "dark",
    "accent_color": "#7c5cff",
    "language": "en_US"
}
```

To modify settings:
1. Open **Settings > Preferences** from the top menu bar.
2. Select your preferred **Theme**, **Accent Color**, and **Language**.
3. Click **Apply & Save**. Changes are applied immediately!

---

## 📄 License

This project is licensed under the [MIT](LICENSE) License. Feel free to use, modify, and distribute.

---

<p align="center">
  Developed by <b>RickHardBR</b> 🚀
</p>
