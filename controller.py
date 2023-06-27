from model import Task
from database import Database

class Controller:
    def __init__(self):
        self.db = Database()

    def add_task(self, task_text):
        task = Task(title=task_text)
        self.db.save_task(task)

    def mark_task_done(self, task_index):
        task = self.db.get_task(task_index)
        if task:
            task.mark_done()
            self.db.update_task(task)
            return True
        return False

    def get_task_list(self):
        return self.db.get_all_tasks()

    def delete_task(self, task_index):
        task = self.db.get_task(task_index)
        if task:
            self.db.delete_task(task)
            return True
        return False