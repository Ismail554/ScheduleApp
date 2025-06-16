subjects_list = []
attendance_records_list = []

class Subject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class AttendanceRecord:
    def __init__(self, subject, date, student_attendance):
        self.subject = subject # Expects a Subject object
        self.date = date
        self.student_attendance = student_attendance

    def __str__(self):
        # Improved __str__ for better display
        return f"Date: {self.date}, Subject: {self.subject.name}, Attendance: {self.student_attendance}"

def add_subject(name):
    """
    Adds a new subject to the subjects_list.
    Checks for duplicates before adding.
    """
    for subject in subjects_list:
        if subject.name.lower() == name.lower():
            print(f"Subject '{name}' already exists.")
            return
    new_subject = Subject(name)
    subjects_list.append(new_subject)
    print(f"Subject '{name}' added successfully.")

def show_subjects():
    """Prints all subjects in subjects_list."""
    if not subjects_list:
        print("No subjects available.")
        return
    print("\n--- Subjects ---")
    for i, subject in enumerate(subjects_list):
        print(f"{i+1}. {subject.name}")
    print("----------------")

def take_attendance(subject_name, date, student_statuses):
    """
    Records attendance for a given subject and date.
    """
    found_subject = None
    for subj in subjects_list:
        if subj.name.lower() == subject_name.lower():
            found_subject = subj
            break

    if not found_subject:
        print(f"Error: Subject '{subject_name}' not found. Cannot record attendance.")
        return

    new_attendance_record = AttendanceRecord(found_subject, date, student_statuses)
    attendance_records_list.append(new_attendance_record)
    print(f"Attendance recorded for {subject_name} on {date}.")

def parse_student_statuses(statuses_str):
    """
    Parses a string like "John:present,Jane:absent" into a dictionary.
    Returns the dictionary or None if parsing fails.
    """
    statuses = {}
    try:
        pairs = statuses_str.split(',')
        if not all(':' in pair for pair in pairs if pair.strip()): # Ensure all non-empty pairs have a colon
             raise ValueError("Invalid format. Each entry must have a colon.")
        for pair in pairs:
            pair = pair.strip()
            if not pair: # Skip empty strings that might result from trailing commas
                continue
            name, status = pair.split(':', 1) # Split only on the first colon
            name = name.strip()
            status = status.strip().lower()
            if not name or status not in ["present", "absent", "late", "excused"]: # Added more valid statuses
                 print(f"Warning: Invalid status '{status}' for student '{name}'. Skipping.")
                 continue
            statuses[name] = status
        return statuses
    except ValueError as e:
        print(f"Error parsing student statuses: {e}. Expected format: 'Name1:Status1,Name2:Status2'.")
        return None


def cli():
    """Main command-line interface for the application."""
    print("Welcome to the Attendance Tracker!")

    while True:
        print("\nAvailable options:")
        print("  1. Add Subject")
        print("  2. Take Attendance")
        print("  3. View Subjects")
        print("  4. View All Attendance")
        print("  5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            subject_name = input("Enter subject name: ").strip()
            if subject_name:
                add_subject(subject_name)
            else:
                print("Subject name cannot be empty.")

        elif choice == '2':
            if not subjects_list:
                print("No subjects available. Please add a subject first.")
                continue
            subject_name = input("Enter subject name for attendance: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            statuses_str = input("Enter student attendance (e.g., John:present,Jane:absent): ").strip()

            if not subject_name or not date or not statuses_str:
                print("Subject name, date, and student statuses cannot be empty.")
                continue

            student_statuses = parse_student_statuses(statuses_str)
            if student_statuses is not None: # Check if parsing was successful (not None)
                if not student_statuses: # Check if the resulting dictionary is empty
                    print("No valid student attendance data was entered.")
                else:
                    take_attendance(subject_name, date, student_statuses)

        elif choice == '3':
            show_subjects()

        elif choice == '4':
            if not attendance_records_list:
                print("No attendance records found.")
            else:
                print("\n--- All Attendance Records ---")
                for i, record in enumerate(attendance_records_list):
                    print(f"{i+1}. {record}") # Relies on the improved __str__
                print("-----------------------------")

        elif choice == '5':
            print("Exiting application.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    # Previous test code commented out or removed
    # add_subject("Physics")
    # add_subject("Chemistry")
    # sample_statuses_physics = {"Alice": "present", "Bob": "absent"}
    # take_attendance("Physics", "2024-07-27", sample_statuses_physics)

    cli() # Start the command-line interface
