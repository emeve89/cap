from entities.todo import Todo


class CreateTodo:

    def execute(self, text):
        todo = Todo(text)
        return todo