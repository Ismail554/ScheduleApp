# Attendance Tracking Application

## Overview

This application provides a command-line interface (CLI) to help track student attendance for various subjects. Users can manage subjects, record daily attendance, and view recorded data.

## Features

*   **Manage Subjects:**
    *   Add new subjects to the tracking list.
    *   View a list of all added subjects.
    *   Prevents duplicate subject entries.
*   **Track Attendance:**
    *   Record attendance for a specific subject on a given date.
    *   Input student attendance using a simple format: `StudentName1:Status1,StudentName2:Status2` (e.g., `Alice:present,Bob:absent,Charlie:late`). Valid statuses include `present`, `absent`, `late`, and `excused`.
*   **View Records:**
    *   Display all attendance records, showing the date, subject, and the status of each student.

## How to Run

1.  **Ensure Python is installed.** This application is written in Python.
2.  **Navigate to the application directory.** Open your terminal or command prompt and change to the directory where `app.py` is located.
3.  **Run the application using the following command:**

    ```bash
    python app.py
    ```

4.  **Navigate the CLI Menu:**
    *   Once started, the application will display a menu of options.
    *   Enter the number corresponding to your desired action (e.g., `1` to Add Subject, `5` to Exit) and press Enter.
    *   Follow the on-screen prompts to input required information.

## Data

*   Subject information and attendance records are stored in memory and will be lost when the application exits. Future versions may include data persistence.
