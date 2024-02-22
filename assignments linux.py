import os
import subprocess

base_location = "Desktop"

def create_new_course():
    course_name = input("Enter course name: ")
    course_folder = f"(){course_name}"
    desktop_path = os.path.join(os.path.expanduser("~"), base_location)
    course_path = os.path.join(desktop_path, course_folder)
    os.makedirs(course_path)
    print(f"Course '{course_name}' created successfully.")

def create_new_assignment():
    desktop_path = os.path.join(os.path.expanduser("~"), base_location)
    courses = [folder for folder in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, folder)) and folder.startswith("()")]
    if not courses:
        print("No courses found. Please create a course first.")
        return

    print("Available courses:")
    for index, course in enumerate(courses, 1):
        print(f"{index}. {course}")

    course_index = int(input("Select a course (enter the number): ")) - 1
    selected_course = courses[course_index]

    assignment_name = input("Enter assignment name: ")
    assignment_folder = f"(){assignment_name}"
    assignment_path = os.path.join(desktop_path, selected_course, assignment_folder)
    os.makedirs(assignment_path)

    os.chdir(assignment_path)
    os.system("git init")
    add_remote = input("Do you want to add a remote git? (y/N): ").strip().lower()
    if add_remote == 'y':
        git_link = input("Enter git URL: ")
        os.system(f"git remote add origin {git_link}")
        os.system("git pull origin main")
        os.system("git branch -m master main")

    print(f"Assignment '{assignment_name}' created successfully.")

def open_assignment():
    desktop_path = os.path.join(os.path.expanduser("~"), base_location)
    courses = [folder for folder in os.listdir(desktop_path) if os.path.isdir(os.path.join(desktop_path, folder)) and folder.startswith("(")]
    if not courses:
        print("No courses found. Please create a course first.")
        return

    print("Available courses:")
    for index, course in enumerate(courses, 1):
        print(f"{index}. {course}")

    course_index = int(input("Select a course (enter the number): ")) - 1
    selected_course = courses[course_index]

    course_path = os.path.join(desktop_path, selected_course)
    assignments = [folder for folder in os.listdir(course_path) if os.path.isdir(os.path.join(course_path, folder))]
    
    if not assignments:
        print("No assignments found in this course.")
        return
    
    if len(assignments) == 1:
        selected_assignment = assignments[0]
    else:
        print("Available assignments:")
        for index, assignment in enumerate(assignments, 1):
            print(f"{index}. {assignment}")
        
        assignment_index = int(input("Select an assignment (enter the number): ")) - 1
        selected_assignment = assignments[assignment_index]
    
    assignment_path = os.path.join(course_path, selected_assignment)
    
   # Construct the command to open a new Terminal window and navigate to the assignment folder
    if os.name == 'posix':  # Unix-like system
        terminal_command = f"gnome-terminal --working-directory='{assignment_path}'"
    else:
        print("Opening a new terminal window is not supported on this platform.")
        return

    # Execute the command
    subprocess.run(terminal_command, shell=True)

    print(f"Opened assignment '{selected_assignment}' in a new Terminal window.")


def main_menu():
    while True:
        print("\nMenu:")
        print("1. Create new Course")
        print("2. Create new Assignment")
        print("3. Open Assignment")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            create_new_course()
        elif choice == '2':
            create_new_assignment()
        elif choice == '3':
            open_assignment()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
