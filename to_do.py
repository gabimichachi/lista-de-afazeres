lista_de_tarefas=[]

print('''------------------' 
    '|  LISTA DE AFAZERES |' 
    '----------------------' 
    '1- inserir tarefas' 
    '2- listar tarefa' 
    '3- marcar como concluido ' 
    '4- remover tarefa ' 
    '--------------------------''')


#perguntando aqui
while True:
    tarefa = int(input("informe o número da tarefa que você deseja realizar: "))

    if tarefa == 1:
        print("você vai inserir a tarefa.")
        lista_de_tarefas.append(tarefa)

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


