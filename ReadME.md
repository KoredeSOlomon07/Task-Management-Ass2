# Task Manager

## Overview

The Task Manager is a Python program designed to help users manage their tasks efficiently. Users can add new tasks, view existing tasks, mark tasks as completed, delete tasks, and receive scheduled notifications for upcoming and overdue tasks.

## Getting Started

1. Installation:
   Clone the repository to your local machine.
   Ensure you have Python installed (version 3.6 or above).
2. Dependencies:
   The system relies on external libraries. Install them using:
   pip3 install tabulate schedule
3. Usage:
   Run the main.py script:
   python main.py
   Follow the on-screen prompts to interact with the TaskManager.

## Features

**User-Friendly Interface:** Users can easily add, view, mark completion, and delete tasks through a simple command-line interface.
**Scheduled Notifications:** The system notifies users of upcoming tasks daily at 09:00 and alerts them about overdue tasks every hour.
**Data Persistence:** Task data is stored in a JSON file (tasks.json) for seamless loading and saving.

## Code Structure

**TaskManager Class:** It serves as a centralized module for task management, implementing key functionalities and overseeing data handling.

## Functions:

**loadTasks:** Loads tasks from the data file.
**saveTasks:** Saves tasks to the data file.
**addTask:** Adds a new task to the system.
**viewTasks:** Displays tasks in a tabulated format.
**markTaskCompleted:** Marks a task as completed.
**deleteTask:** Deletes a task from the system.
**setup_notifications:** Sets up scheduled notifications.

## Requirements

- Python 3.x
- `tabulate` library (install using `pip3 install tabulate`)
- `schedule` library (install using `pip3 install schedule`)

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies (`tabulate` and `schedule`) using `pip or pip3`.
3. Run the program by executing command.
4. Follow the on-screen prompts to interact with the Task Manager.

## Functionality Details

- The program stores tasks in a JSON file (`tasks.json`) for persistent data storage.
- Users can add tasks, providing an optional due time for better organization.
- The program provides an overview of tasks in a tabular format.
- Scheduled notifications inform users of upcoming and overdue tasks.
- Users can mark tasks as completed or delete them as needed.

## USER INTERACTION:

- RUN THE CODE

## RESPONSE:

Task Management System

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Quit
   Enter your choice (1-5):

## User Input: 1

Enter the task: Complete Project Proposal
Enter the due time in HH:MM format (optional, press Enter to skip): 2022-02-15 12:00

## User Input: 2

IT PROVIDE THE TASKED IN A TABULE FORMAT

## User Input: 3

User Prompt: Enter the task index to mark as completed: 1

## RESPONSE:

Task 1 marked as completed.
