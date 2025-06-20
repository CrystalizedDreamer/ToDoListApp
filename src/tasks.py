class Task_Manager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the task list."""
        self.tasks.append(task)

    def view_tasks(self):
        """Return the list of current tasks."""
        return self.tasks

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            return True
        return False