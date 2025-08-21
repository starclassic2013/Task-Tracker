import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json
from pathlib import Path

DATA_DIR = Path.home() / ".task_tracker"
DATA_DIR.mkdir(parents=True, exist_ok=True)
TASKS_FILE = DATA_DIR / "tasks.json"

class App(tk.Tk):
    def __init__(self):
        
        
        super().__init__()
        self.geometry("1000x800")
        self.configure(bg = "lightblue")
        
        frame = ttk.Frame(self)
        frame.pack(pady = 10)
        
        label = tk.Label(frame, text = "Task Tracker", font = ("Helvetica", 30))
        label.pack(pady = 5)
        
        self.entry = ttk.Entry(frame, width = 30)
        self.entry.pack(side = "left", padx = 20, pady = 5)
        
        self.addbutton = ttk.Button(frame, text = "Add Task", command = self.on_click)
        self.addbutton.pack(side = "left", pady = 5)
        
        self.deletebutton = ttk.Button(frame, text = "Delete Task", command = self.click_on)
        self.deletebutton.pack(side = "left", pady = 5, padx = 5)
        
        self.tree = ttk.Treeview(self, columns = ("Task", "Due Date", "Notes"), show = "headings")
        self.tree.heading("Task", text = "Task")
        self.tree.heading("Due Date", text = "Due Date")
        self.tree.heading("Notes", text = "Notes")
        
        self.tree.pack(padx = 10, pady = 5, fill = "both", expand = True)
        
        self.load_tasks()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
    def on_click(self):
        task = self.entry.get().strip()
        
        if not task:
            return
        
        due_date = simpledialog.askstring("Due Date", "Enter due date (DD-MM-YYYY)", parent = self) or ""
        
       
        
        notes = simpledialog.askstring("Notes", "Input additional Notes", parent = self)
        
        
        self.tree.insert("", "end", values=(task, due_date, notes))
        self.entry.delete(0, tk.END)
        self.save_tasks()
        
    def click_on(self):
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("No Selection", "Select a Task To Delete")
            return
        self.tree.delete(*selection)
        self.save_tasks()
        
    def load_tasks(self):
        
        if not TASKS_FILE.exists():
            return
        
        try:
            data = json.loads(TASKS_FILE.read_text(encoding = "utf-8"))
            
            for item in data:
                self.tree.insert("", "end", values=(item.get("task", ""), item.get("due", ""), item.get("notes", "")))
                
        except json.JSONDecodeError:
            messagebox.showwarning("Data Error", f"Couldn't read {TASKS_FILE.name}. Starting with an empty list.")
            
    def save_tasks(self):
        
        rows = []
        
        for iid in self.tree.get_children(""):
            task, due, notes = self.tree.item(iid, "values")
            rows.append({"task": task, "due": due, "notes": notes})
            
        TASKS_FILE.write_text(json.dumps(rows, indent = 2), encoding="utf-8")
        
        
    def on_close(self):
        self.save_tasks()
        self.destroy()
        
        
        

        
if __name__ == "__main__":
    app = App()
    app.mainloop()
        