from classe_tarefa import Tarefa

tarefas = Tarefa()

print('''------------------' 
    '|  LISTA DE AFAZERES |' 
    '----------------------' 
    '1- inserir tarefas'   |
    '2- listar tarefa'     |
    '3- marcar como concluido ' |
    '4- remover tarefa |
    '0- sair |
    '--------------------------''')


#perguntando aqui
while True:
    tarefa = int(input("informe o número da tarefa que você deseja realizar: "))

    if tarefa == 1:
        tarefas.adicionar_tarefa()
    elif tarefa == 2:
        print("você vai listar a tarefa.")

    elif tarefa == 3:
        print("você vai marcar como concluído.")

    elif tarefa == 4:
        print("você deve renovar a tarefa.")

    elif tarefa == 0:
        print("você acabou as tarefas.")
    else: 

        print("este número não existe.")
        break


