class Task:
    def __init__(self, title, description='', status='Невыполнена'):
        self.title = title
        self.description = description
        self.status = status

    def mark_done(self):
        self.status = 'Выполнена'