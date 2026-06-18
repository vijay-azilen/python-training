class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title, description):
        task = {
            'title': title,
            'description': description
        }
        self.tasks.append(task)
    
    def view_tasks(self):
        return self.tasks