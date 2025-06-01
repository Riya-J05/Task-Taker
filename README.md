# 🧾 Task Tracker CLI

A beginner-friendly, command-line task manager built with Python to help you track your tasks easily. Add, update, delete, and list your to-do items from the terminal with persistent storage using JSON.

---

## 🚀 Features

- ✅ Add new tasks with descriptions and status
- 🔄 Update or delete existing tasks
- 🗂️ View all tasks or filter by status:
  - **To-do**
  - **In-progress**
  - **Completed**
- 💾 Persistent storage using a local JSON file
- 📆 Automatic handling of `createdAt` and `updatedAt` timestamps *(optional extension)*
- 🧱 Built using only native Python modules — no third-party libraries

---

## 🖥️ Getting Started


### 1. Clone the repo

```bash
git clone https://github.com/your-username/task-tracker-cli.git
cd task-tracker-cli
```

### 2. Run the program

```bash
python task_tracker.py
```


🧑‍💻 Sample Usage
Here’s how the menu works interactively:
========= MENU =========
1. Show all Tasks
2. Show all Completed Tasks
3. Show all In-Progress Tasks
4. Show all Incomplete Tasks
5. Add a Task
6. Update a Task
7. Delete a Task
8. Exit the program


📁 Task Structure
- Each task is stored in JSON format with the following fields:
- {
  "id": 1,
  "desc": "Buy groceries",
  "status": "in-progress"
}


⚙️ Tech Stack
- Language: Python
- File storage: JSON
- Interface: Command Line (CLI)


📌 Project Requirements (from roadmap.sh)
- Accept user inputs and commands from terminal
- Store tasks in a JSON file
- Handle user actions: add, update, delete, list
- Filter tasks by their status (done, in-progress, todo)
- Handle file not found and invalid inputs gracefully


🛠️ Future Improvements
- Add support for timestamps (createdAt, updatedAt)
- Convert to a true command-line tool with argparse
- Add unit tests


 🙌 Acknowledgments
- This project is inspired by the roadmap.sh "Task Tracker" CLI project challenge.
- URL of the project: https://roadmap.sh/projects/task-tracker
