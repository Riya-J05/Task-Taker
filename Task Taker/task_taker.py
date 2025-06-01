import json # JSON lib -> for file handling
import os # OS lib -> for absolute path 

class Task:
  # Tuple containing possible task status 
  task_status = ("completed", "in-progress", "incomplete")
  
  # Constructor
  def __init__(self, id, desc, status): #created_at, updated_at will be added later on!
    self.id = id
    self.desc = desc
    self.status = status
    
  # Converts details of a task obj to a dict
  def to_dict(self):
    return {
      "id": self.id,
      "desc": self.desc,
      "status": self.status
    }
    
# Contains all tasks in a dictionary    
tasks_dict = {}

# Absolute path for file handling
abs_path = os.path.abspath("data")
     
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

# Creates a JSON file and write all tasks to it
def write_file(tasks_dict):
  with open(abs_path + "/tasks_data.txt", "w") as file:
    json.dump(tasks_dict, file, indent=4)
    
# Reading from a JSON file and loading all tasks from it
def read_file():
  with open(abs_path + "/tasks_data.txt", "r") as file:
    tasks_dict = json.load(file)
    return tasks_dict
  
# Verifies that the user enters an appropriate task status
def status_verification():
  given_status = input("Choose a status for your task (completed, in-progress, incomplete): ")
  while given_status.lower() not in Task.task_status:
    given_status = input("Inappropriate choice! Please choose a legitimate status (completed, in-progress, incomplete): ")
  return given_status.lower()
  
# Shows all the tasks 
def show_all_tasks(tasks_dict):
  print(f"\n{"ID":<10} {"DESCRIPTION":<20} {"STATUS"}")
  for key in tasks_dict:
    print(f"{tasks_dict[key]["id"]:<10} {tasks_dict[key]["desc"]:<20} {tasks_dict[key]["status"]}")

# Shows specific tasks based on their status
def show_specific_tasks(tasks_dict, task_status):
  print(f"\n{"ID":<10} {"DESCRIPTION":<20} {"STATUS"}")
  for key in tasks_dict:
    if (tasks_dict[key]["status"] == task_status.lower()):
      print(f"{tasks_dict[key]["id"]:<10} {tasks_dict[key]["desc"]:<20} {tasks_dict[key]["status"]}")
      
# Adds a task
def add_task(tasks_dict):
  task_id = int(input("Enter the id number of your task: "))
  if(str(task_id) in tasks_dict):
    print("A task with this id already exists!")
  else:
    task_desc = input("Enter the description of your task: ")
    # Checking of the user is choosing an appropriate task status
    task_status = status_verification()
    new_task = Task(task_id, task_desc, task_status) # Initialising a task object
    tasks_dict[new_task.id] = new_task.to_dict() # Adds task to tasks_dict using id as key
    print("Task added successfully!")
    # Updating the JSON file
    write_file(tasks_dict)

# Updates a task
def update_task(tasks_dict):
  show_all_tasks(tasks_dict)
  upd_id = input("\nEnter the id of the task you want to update: ")
  # If key is present in the dict
  if (upd_id in tasks_dict):
    del tasks_dict[upd_id] # deletes the old entry
    # Gets the updated tasks' info
    new_id = int(input("Enter the updated task id: "))
    new_desc = input("Enter the updated task description: ")
    new_status = status_verification() # Verifying task status entered by user
    new_task = Task(new_id, new_desc, new_status) # Initialising a task object
    tasks_dict[new_id] = new_task.to_dict() # Adds task to tasks_dict using id as key
    print("Task updated successfully!")
  else:
    print("Task not found!")
  # Updating the JSON file
  write_file(tasks_dict)

# Deletes a task
def delete_task(tasks_dict):
  show_all_tasks(tasks_dict)
  del_id = input("\nEnter the id of the task you want to delete: ")
  if (del_id in tasks_dict):
    del tasks_dict[del_id]
    print("Task deleted successfully!")
  else:
    print("Task not found!")
# Updating the JSON file
  write_file(tasks_dict)

# MAIN PROGRAM 
def main():
  run = "y"
  while run.lower() == "y":
    # Error handling
    try:
      # Loads tasks from the dict 
      tasks_dict = read_file()
    # Catching the filenotfound error
    except FileNotFoundError:
      tasks_dict = {}
    
    # Handling other unexpected errors
    try:
      # Displaying the menu
      menu()
      # Asking the user for an option
      op = int(input("Enter the menu option: "))
      
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
    
    # Catching exceptions
    except ValueError:
      print("Oops! That was not a valid input value. Try again...")
    
    except:
      print("Unexpected error happened!")
      
      
if __name__ == "__main__":
  main()