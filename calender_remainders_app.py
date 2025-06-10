import tkinter as tk
from tkinter import simpledialog, messagebox
import calendar
from datetime import datetime
import json
import os

REMINDER_FILE = "reminders.json"

# Load reminders from file
def load_reminders():
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save reminders to file
def save_reminders(reminders):
    with open(REMINDER_FILE, 'w') as file:
        json.dump(reminders, file, indent=4)

# Calendar App Class
class CalendarReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar with Reminders")
        self.now = datetime.now()
        self.current_year = self.now.year
        self.current_month = self.now.month
        self.reminders = load_reminders()
        self.build_calendar()

    def build_calendar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        cal = calendar.monthcalendar(self.current_year, self.current_month)

        header = tk.Label(self.root, text=f"{calendar.month_name[self.current_month]} {self.current_year}", font=("Arial", 16))
        header.grid(row=0, column=1, columnspan=5)

        tk.Button(self.root, text="<", command=self.prev_month).grid(row=0, column=0)
        tk.Button(self.root, text=">", command=self.next_month).grid(row=0, column=6)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.root, text=day, font=("Arial", 10, "bold")).grid(row=1, column=i)

        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day != 0:
                    date_key = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
                    has_reminder = date_key in self.reminders
                    btn = tk.Button(self.root, text=str(day), width=5,
                                    bg="lightblue" if has_reminder else None,
                                    command=lambda d=day: self.set_reminder(d))
                    btn.grid(row=week_num + 2, column=day_num)

    def prev_month(self):
        self.current_month -= 1
        if self.current_month == 0:
            self.current_month = 12
            self.current_year -= 1
        self.build_calendar()

    def next_month(self):
        self.current_month += 1
        if self.current_month == 13:
            self.current_month = 1
            self.current_year += 1
        self.build_calendar()

    def set_reminder(self, day):
        date_key = f"{self.current_year}-{self.current_month:02d}-{day:02d}"
        current = self.reminders.get(date_key, "")
        result = simpledialog.askstring("Set Reminder", f"Reminder for {date_key}:", initialvalue=current)

        if result is not None:
            if result.strip() == "":
                self.reminders.pop(date_key, None)
            else:
                self.reminders[date_key] = result.strip()
            save_reminders(self.reminders)
            self.build_calendar()

# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarReminderApp(root)
    root.mainloop()
