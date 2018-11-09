from entities.todo import Todo


class ToggleTodoStatus:

    def __init__(self):
        self.todo = Todo("Complete this example App")

    def execute(self):
        return self.todo.toggle_status()

    # TODO: Just to print the todo's status. MUST BE REMOVED FROM USE CASE PACKAGE
    def print_status(self):
        return self.todo.status