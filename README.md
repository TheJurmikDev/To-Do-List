---

# To-Do List with Memory

## 🚀 About
**To-Do List with Memory** is a simple Python-based to-do list application that allows users to add, remove, and view tasks. The app stores tasks in a text file and provides a simple menu-driven interface for interacting with the list. This project is a good exercise for learning file handling and basic Python programming.

## 🛠️ Features
- **Add Tasks**: Add new tasks to the to-do list.
- **Remove Tasks**: Remove tasks by specifying the line number.
- **View Tasks**: View the current to-do list stored in a text file.
- **Simple Menu**: Easy-to-use text-based menu for interacting with the list.

## ⚙️ Requirements
- Python 3.x
- Basic knowledge of Python and file handling.

## 📥 Installation & Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/ToDo-List-With-Memory.git
    cd ToDo-List-With-Memory
    ```

2. Run the application:
    ```bash
    python todo_list.py
    ```

3. Follow the on-screen menu to add, remove, or view tasks.

## 🔧 How It Works
The application reads from and writes to a file called `list.txt` where the to-do list items are stored. The main functions of the program are:
- `data_get()` – Reads and returns the content of the to-do list file.
- `data_write(data)` – Appends new tasks to the list.
- `data_remove(line_index_to_delete)` – Removes a task from the list by its line index.
- `menu_main()` – The main menu function that allows users to choose between adding, removing, or viewing tasks.

## ⚠️ Disclaimer
- The project does not have advanced error handling. Ensure that the `list.txt` file exists and is not corrupted for smooth functionality.
- The line indexing starts from 0, so be careful when removing tasks.

---
