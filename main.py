user_prompt = "Enter a Todo: "

todos = []

while True:
    todo = input(user_prompt)
    todos.append(todo.capitalize())
    print(todos)

