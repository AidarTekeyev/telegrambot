import sqlite3
from model import Task

DB_FILENAME = 'tasks.db'


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(DB_FILENAME)
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    description TEXT,
                    status TEXT
                )'''
        self.conn.execute(query)

    def save_task(self, task):
        query = 'INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)'
        self.conn.execute(query, (task.title, task.description, task.status))
        self.conn.commit()

    def update_task(self, task):
        query = 'UPDATE tasks SET title=?, description=?, status=? WHERE id=?'
        self.conn.execute(query, (task.title, task.description, task.status, task.id))
        self.conn.commit()

    def get_task(self, task_id):
        query = 'SELECT * FROM tasks WHERE id=?'
        cursor = self.conn.execute(query, (task_id,))
        row = cursor.fetchone()
        if row:
            task = Task(title=row[1], description=row[2], status=row[3])
            task.id = row[0]
            return task
        return None

    def get_all_tasks(self):
        query = 'SELECT * FROM tasks'
        cursor = self.conn.execute(query)
        tasks = []
        for row in cursor:
            task = Task(title=row[1], description=row[2], status=row[3])
            task.id = row[0]
            tasks.append(task)
        return tasks

    def delete_task(self, task):
        query = 'DELETE FROM tasks WHERE id=?'
        self.conn.execute(query, (task.id,))
        self.conn.commit()