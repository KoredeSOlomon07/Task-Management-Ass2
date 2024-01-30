import json
import os
from tabulate import tabulate
from datetime import datetime, timedelta
import schedule
import time


class TaskManager:
    def __init__(self, data_file='tasks.json'):
        self.data_file = data_file
        self.tasks = self.loadTasks()
        self.setup_notifications()

    def loadTasks(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def saveTasks(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.tasks, file, indent=2)

# This function adds a new task with a description, completion status, optional due time, and a timestamp to the task list, saving the updated list to a data file and printing a success message.
    def addTask(self, task, due_time=None):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.tasks.append({'task': task, 'completed': False,
                          'due_time': due_time, 'timestamp': timestamp})
        self.saveTasks()
        print(f"Task '{task}' added successfully!")
# This Function make it Possible for us to view the task list

    def viewTasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            table_data = [(i + 1, task['task'], 'Completed' if task['completed'] else 'Not Completed', task.get(
                'due_time', 'N/A'), task.get('timestamp', 'N/A')) for i, task in enumerate(self.tasks)]
            headers = ["ID", "Task", "Status", "Due Time", "Timestamp"]
            table = tabulate(table_data, headers, tablefmt="fancy_grid")
            print(table)

    # this function Mark an incomplete task as completed after the task is been met
    def markTaskCompleted(self, taskIndex):
        try:
            taskIndex = int(taskIndex)
            if 1 <= taskIndex <= len(self.tasks):
                self.tasks[taskIndex - 1]['completed'] = True
                self.saveTasks()
                print(f"Task {taskIndex} marked as completed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid task index. Please enter a number.")

# This function Delete a task from the tasklist
    def deleteTask(self, taskIndex):
        try:
            taskIndex = int(taskIndex)
            if 1 <= taskIndex <= len(self.tasks):
                deletedTask = self.tasks.pop(taskIndex - 1)
                self.saveTasks()
                print(f"Task {taskIndex} deleted: {deletedTask['task']}")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid task index. Please enter a number.")

    def setup_notifications(self):
        # Schedule upcoming task notification every day at 09:00
        schedule.every().day.at("09:00").do(self.check_and_notify_upcoming_tasks)
        # Schedule overdue task notification every hour
        schedule.every().hour.do(self.check_and_notify_overdue_tasks)

    def check_and_notify_upcoming_tasks(self):
        # Get the current datetime
        now = datetime.now()
        for task in self.tasks:
            # Check if the task has a due time
            if 'due_time' in task and task['due_time'] is not None:
                # Convert the task's due time to a datetime object
                due_time = datetime.strptime(
                    task['due_time'], '%Y-%m-%d %H:%M:%S')
                # If the task is due today or in the future notify the user
                if now < due_time <= now + timedelta(days=1):
                    print(f"Upcoming task: {task['task']} is due soon. Due Time: {
                          task['due_time']}")

    def check_and_notify_overdue_tasks(self):
        now = datetime.now()
        for task in self.tasks:
            if 'due_time' in task and task['due_time'] is not None:
                due_time = datetime.strptime(
                    task['due_time'], '%Y-%m-%d %H:%M:%S')
                if due_time < now and not task['completed']:
                    print(f"Overdue task: {task['task']}! Due Time: {
                          task['due_time']}")

    def check_real_time_notifications(self):
        now = datetime.now().strftime('%H:%M')
        for task in self.tasks:
            if 'due_time' in task and task['due_time'] is not None and task['due_time'] == now:
                print(
                    f"Notification : It's time to do task '{task['task']}' don't be Lazy!")


def main():
    taskManager = TaskManager()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            due_time = input(
                "Enter the due time in HH:MM format (optional, press Enter to skip): ")
            due_time = due_time if due_time else None
            taskManager.addTask(task, due_time)
        elif choice == '2':
            taskManager.viewTasks()
        elif choice == '3':
            taskIndex = input("Enter the task index to mark as completed: ")
            taskManager.markTaskCompleted(taskIndex)
        elif choice == '4':
            taskIndex = input("Enter the task index to delete: ")
            taskManager.deleteTask(taskIndex)
        elif choice == '5':
            print("Quitting. Goodbye!")
            break
        else:
            print("Invalid Number. Please enter between 1 and 5.")

        # Check for scheduled notifications every minute
        schedule.run_pending()

        # Check real-time notifications every second
        taskManager.check_real_time_notifications()

        # Sleep for a short time to avoid high CPU usage in the loop
        time.sleep(1)


if __name__ == "__main__":
    main()
