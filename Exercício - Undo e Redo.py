"""
Faça uma lista de tarefas com as seguintes opções:
    1- Adicionar tarefa
    2- Listar tarefas
    3- Desfazer a última ação
    4- Refazer a última ação
"""

def show_op(todo_list):
    print("Tarefas:")
    print(todo_list)

def do_add(todo, todo_list):
    todo_list.append(todo)
    
def do_undo(todo_list, redo_list):
    if not todo_list:
        print("Nada a desfazer.")
        return
    
    last_todo = todo_list.pop()
    redo_list.append(last_todo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print("Nada a refazer.")
        return
    
    last_redo = redo_list.pop()
    todo_list.append(last_redo)

if __name__ == "__main__":
    todo_list = []
    redo_list = []
    
    while True:
        todo = input("Digite uma nova tarefa ou os comandos \"undo\", \"redo\" e \"listar\": ")
        
        if todo == "listar":
            show_op(todo_list)
            continue
        elif todo == "undo":
            do_undo(todo_list, redo_list)
            continue
        elif todo == "redo":
            do_redo(todo_list, redo_list)
            continue
        
        do_add(todo, todo_list)
        
        