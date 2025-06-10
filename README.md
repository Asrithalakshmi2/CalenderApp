# Python Calendar with Reminders

A simple desktop calendar application with reminder functionality, built using Python's Tkinter library. This application allows users to view a calendar, set reminders for specific dates, and saves these reminders for persistence.

## Features

* **Interactive Calendar Display**: Navigates through months and years.
* **Set Reminders**: Easily add or edit reminders for any date.
* **Reminder Persistence**: Reminders are saved to a `reminders.json` file, so they are not lost when the application is closed.
* **Visual Cues**: Dates with reminders are highlighted on the calendar.
* **User-Friendly Interface**: Built with Tkinter for a straightforward graphical user interface.

## Files

* `calender_remainders_app.py`: The main Python script containing the application logic and Tkinter UI.
* `reminders.json`: A JSON file where all your reminders are stored. This file is automatically created if it doesn't exist.

## Requirements

This application uses standard Python libraries and `tkinter` which usually comes pre-installed with Python. No additional installations are typically required.

## How to Run

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [https://github.com/YourUsername/your-calendar-app-repo.git](https://github.com/YourUsername/your-calendar-app-repo.git)
    cd your-calendar-app-repo
    ```
    (Replace `YourUsername` and `your-calendar-app-repo` with your actual GitHub username and repository name.)

2.  **Run the Python script:**
    ```bash
    python calender_remainders_app.py
    ```

## Usage

1.  **Navigate Calendar**: Use the "<" and ">" buttons to move to the previous and next months.
2.  **Set/Edit Reminder**: Click on any day number on the calendar to open a dialog box.
    * Enter your reminder text and click "OK" to save it.
    * If a reminder already exists, it will be shown in the dialog, and you can edit it.
    * To delete a reminder, clear the text in the dialog box and click "OK".
3.  **Reminder Indication**: Dates with set reminders will be highlighted in light blue.

## Project Structure

* `calender_remainders_app.py`:
    * `load_reminders()`: Loads reminders from `reminders.json`.
    * `save_reminders(reminders)`: Saves current reminders to `reminders.json`.
    * `CalendarReminderApp` class:
        * `__init__`: Initializes the Tkinter window and loads existing reminders.
        * `build_calendar()`: Dynamically creates and updates the calendar display.
        * `prev_month()`: Handles navigation to the previous month.
        * `next_month()`: Handles navigation to the next month.
        * `set_reminder(day)`: Prompts the user to set/edit/delete a reminder for the selected day.
* `reminders.json`: Stores reminders in a JSON format (e.g., `{"YYYY-MM-DD": "Your Reminder Text"}`).

## Example `reminders.json`

```json
{
    "2025-07-02": "Asritha's day",
    "2025-06-15": "Project Deadline",
    "2025-06-20": "Team Meeting"
}
