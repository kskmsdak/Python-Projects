import json
import os
import sys

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "status": "not done"}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def update_task(task_id, description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            save_tasks(tasks)
            print("Task updated.")
            return
    print("Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print("Task deleted.")

def mark_task_progress(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'in progress'
            save_tasks(tasks)
            print("Task marked as in progress.")
            return
    print("Task not found.")

def mark_task_done(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            save_tasks(tasks)
            print("Task marked as done.")
            return
    print("Task not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    for task in tasks:
        if status is None or task['status'] == status:
            print(f"[{task['status']}] {task['id']}: {task['description']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "add":
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "update":
        task_id = int(sys.argv[2])
        description = " ".join(sys.argv[3:])
        update_task(task_id, description)
    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == "in_progress":
        task_id = int(sys.argv[2])
        mark_task_progress(task_id)
    elif command == "done":
        task_id = int(sys.argv[2])
        mark_task_done(task_id)
    elif command == "list":
        list_tasks()
    elif command == "list_done":
        list_tasks("done")
    elif command == "list_not_done":
        list_tasks("not done")
    elif command == "list_in_progress":
        list_tasks("in progress")
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()