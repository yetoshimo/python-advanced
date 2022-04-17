from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in map(lambda n: n.name, self.tasks):
            return f"Could not find task with the name {task_name}"
        next(filter(lambda n: n.name == task_name, self.tasks)).completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        _counter = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                _counter += 1
        return f"Cleared {_counter} tasks."

    def view_section(self):
        _view_details = f"Section {self.name}:\n"
        for d in self.tasks:
            _view_details += f"{d.details()}\n"
        return _view_details
