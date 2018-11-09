from usecases.create_todo import CreateTodo

if __name__ == '__main__':
    todo = CreateTodo().execute("COMPLETE EXAMPLE APP")
    print(todo.status)
