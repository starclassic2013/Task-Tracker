# Task-Tracker
A simple desktop task tracker built with Python’s Tkinter. Add tasks, optionally capture a due date and notes, and persist them to disk between sessions.

Features

Add a task via the input box; due date & notes are prompted with dialogs

Delete selected task(s)

Auto-save to a JSON file on every change and on exit

Restores tasks on launch

Portable single-file script

Requirements

Python 3.9+

Standard library only (no third-party deps)

Uses: tkinter, ttk, json, pathlib

Installation & Run

Save the script (e.g., task_tracker.py).

Run:

python task_tracker.py

How It Works
UI

Entry field: type the task title, then click Add Task.

On add, you’ll see two dialogs:

Due Date: free-form text (e.g., 20-08-2025). Validation is not enforced.

Notes: optional notes (can be left blank).

Delete Task removes the currently selected row(s) in the table.

Window close (X) triggers a final save.

Data Persistence

Saves to:
Windows/macOS/Linux: ~/.task_tracker/tasks.json

Directory is created automatically if missing.

JSON shape:

[
  { "task": "Buy screws", "due": "21-08-2025", "notes": "Brass, #8" },
  { "task": "Email vendor", "due": "", "notes": "" }
]

File/Folder Details

Data directory: ~/.task_tracker/

Data file: tasks.json

Behavior if missing/invalid: starts with an empty list; shows a warning if the JSON cannot be parsed.

Keyboard & Tips

Enter after typing a task then click Add Task (no direct Enter-to-add binding in this script).

You can select multiple tasks in the table (Ctrl/Cmd-click) and delete them at once.

To clear everything: close the app and delete ~/.task_tracker/tasks.json.

Known Limitations (and easy upgrades)

No in-table editing: Due date/notes can’t be edited directly after creation.

Upgrade idea: bind a double-click on a row to re-open dialogs and update values.

No date validation: The due date is stored as typed.

Upgrade idea: validate against DD-MM-YYYY and/or offer a calendar picker.

No sorting/filtering: Everything is displayed as added.

Upgrade idea: add column sorting and a search box.

Packaging as a Windows .exe (optional)

Use PyInstaller:

Install:

pip install pyinstaller


Build a single-file executable:

pyinstaller --onefile --windowed task_tracker.py


Your exe will be in the dist/ folder (e.g., dist/task_tracker.exe).
--windowed prevents a console window from opening.
Data will still be saved to ~/.task_tracker/tasks.json.

If you see antivirus or SmartScreen warnings, code-signing the exe or distributing the .py file may be preferable.

Troubleshooting

“No Selection” warning while deleting: Select at least one row before pressing Delete Task.

JSON read error on launch: The data file is corrupt. Delete ~/.task_tracker/tasks.json (you’ll lose saved tasks).

Fonts/Theme look off: Tkinter uses platform themes; appearance can vary by OS.

Code Map (quick tour)

App.__init__: builds the UI, loads tasks, wires window close handler

on_click: reads the task entry, asks for due date & notes, inserts into the tree, saves

click_on: deletes selected rows, saves

load_tasks: reads JSON and populates the tree

save_tasks: serializes tree rows to JSON

on_close: saves then destroys the window

License

Choose your license (e.g., MIT) and add it here.

Roadmap (optional)

Inline cell editing for Due/Notes

Date validation & calendar widget

Column sorting and search/filter

Export/Import CSV

Dark mode toggle

Credits

Built with Python’s standard tkinter and ttk.
