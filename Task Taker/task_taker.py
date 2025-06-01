import json  # JSON module for file handling
import os    # OS module for absolute path management

# Task class to define task structure and convert it to dictionary
class Task:
  task_status = ("completed", "in-progress", "incomplete")  # Allowed task statuses

  def __init__(self, id, desc, status):  # Task constructor
    self.id = id
    self.desc = desc
    self.status = status

  def to_dict(self):  # Convert Task object to dictionary format
    return {
      "id": self.id,
      "desc": self.desc,
      "status": self.status
    }

tasks_dict = {}  # Dictionary to hold all tasks
abs_path = os.path.abspath("data")  # Absolute path for file storage

# Displays the main menu
def menu():
  print(f"\n{" MENU ":=^29}")
  print("1. Show all Tasks")
  print("2. Show all Completed Tasks")
  print("3. Show all In-Progress Tasks")
  print("4. Show all Incomplete Tasks")
  print("5. Add a Task")
  print("6. Update a Task")
  print("7. Delete a Task")
  print("8. Exit the program\n")

# Write tasks to JSON file
def write_file(tasks_dict):
  with open(abs_path + "/tasks_data.txt", "w") as file:
    json.dump(tasks_dict, file, indent=4)

# Read tasks from JSON file
def read_file():
  with open(abs_path + "/tasks_data.txt", "r") as file:
    tasks_dict = json.load(file)
    return tasks_dict

# Prompt and validate status input from user
def status_verification():
  given_status = input("Choose a status for your task (completed, in-progress, incomplete): ")
  while given_status.lower() not in Task.task_status:
    given_status = input("Inappropriate choice! Please choose a legitimate status (completed, in-progress, incomplete): ")
  return given_status.lower()

# Display all tasks
def show_all_tasks(tasks_dict):
  print(f"\n{"ID":<10} {"DESCRIPTION":<20} {"STATUS"}")
  for key in tasks_dict:
    print(f"{tasks_dict[key]["id"]:<10} {tasks_dict[key]["desc"]:<20} {tasks_dict[key]["status"]}")

# Display tasks filtered by status
def show_specific_tasks(tasks_dict, task_status):
  print(f"\n{"ID":<10} {"DESCRIPTION":<20} {"STATUS"}")
  for key in tasks_dict:
    if (tasks_dict[key]["status"] == task_status.lower()):
      print(f"{tasks_dict[key]["id"]:<10} {tasks_dict[key]["desc"]:<20} {tasks_dict[key]["status"]}")

# Add a new task
def add_task(tasks_dict):
  task_id = int(input("Enter the id number of your task: "))
  if(str(task_id) in tasks_dict):
    print("A task with this id already exists!")
  else:
    task_desc = input("Enter the description of your task: ")
    task_status = status_verification()  # Validate task status
    new_task = Task(task_id, task_desc, task_status)  # Create new task
    tasks_dict[new_task.id] = new_task.to_dict()  # Add to dictionary
    print("Task added successfully!")
    write_file(tasks_dict)  # Save to file

# Update an existing task
def update_task(tasks_dict):
  show_all_tasks(tasks_dict)
  upd_id = input("\nEnter the id of the task you want to update: ")
  if (upd_id in tasks_dict):  # If task exists
    del tasks_dict[upd_id]  # Remove old task
    new_id = int(input("Enter the updated task id: "))
    new_desc = input("Enter the updated task description: ")
    new_status = status_verification()  # Validate new status
    new_task = Task(new_id, new_desc, new_status)
    tasks_dict[new_id] = new_task.to_dict()
    print("Task updated successfully!")
  else:
    print("Task not found!")
  write_file(tasks_dict)  # Save updates

# Delete a task by ID
def delete_task(tasks_dict):
  show_all_tasks(tasks_dict)
  del_id = input("\nEnter the id of the task you want to delete: ")
  if (del_id in tasks_dict):
    del tasks_dict[del_id]
    print("Task deleted successfully!")
  else:
    print("Task not found!")
  write_file(tasks_dict)  # Save after deletion

# Main function to run the CLI app
def main():
  run = "y"
  while run.lower() == "y":
    try:
      tasks_dict = read_file()  # Try reading tasks from file
    except FileNotFoundError:
      tasks_dict = {}  # If file doesn't exist, start with empty dict

    try:
      menu()  # Show the menu
      op = int(input("Enter the menu option: "))  # Get user choice

      if (op == 1):
        show_all_tasks(tasks_dict)
      elif (op == 2):
        show_specific_tasks(tasks_dict, "completed")
      elif (op == 3):
        show_specific_tasks(tasks_dict, "in-progress")
      elif (op == 4):
        show_specific_tasks(tasks_dict, "incomplete")
      elif (op == 5):
        add_task(tasks_dict)
      elif (op == 6):
        update_task(tasks_dict)
      elif (op == 7):
        delete_task(tasks_dict)
      elif (op == 8):
        run = "n"
        print("Exiting from the program...")
      else:
        print("Incorrect menu option! Try again...")

    except ValueError:
      print("Oops! That was not a valid input value. Try again...")
    except:
      print("Unexpected error happened!")

# Entry point
if __name__ == "__main__":
  main()
