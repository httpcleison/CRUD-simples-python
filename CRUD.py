#lista de alunos
alunos = {
    'sala1': ["Amanda", "Julio", "Maria", "Roberto"],
    'sala2': ["Pedro", "Cris", "Juliana", "Roberta"],
    'sala3': ["Suzy", "Yuri", "Ster", "Laura"]
}

#create - adiconar um novo aluno
def Create():
    salaPes = input("Digite a sala: ")
    aluno = input("Digite o nome do novo aluno: ")
    alunos[salaPes].append(aluno)
    # print(alunos[salaPes])

#read - retornar endereço do aluno
def Read():
    alunoBuscar = input("Digite o nome de um aluno: ")
    for sala, aluno in alunos.items():
        #se for encontrado o valor da variavel alunoBuscar for encontrada no diconario alunos
        if alunoBuscar in aluno:
            print(f"Aluno(a) {alunoBuscar}, encontrado(a) na {sala}")
            # print(alunos[sala])
            break #finalização do loop

    #se caso a variavel alunoBuscar não for encontrada no dicionario alunos
    if not alunoBuscar in aluno:
        print(f"Aluno(a) {alunoBuscar} não encontrado em nenhuma sala.")

#update - atualizar o nome do aluno
def Update():
    salaPes = input("Digite a sala: ")
    for sala, alunoo in alunos.items():
        #se a sala for encontrada
        if salaPes in sala:
            aluno = input("Digite o nome do aluno: ")
            #se for encontrado um aluno na sala(salaPes)
            if aluno in alunoo:
                index_aluno = alunos[sala].index(aluno)
                newAluno = input("Digite o nome do novo aluno: ")
                alunos[sala][index_aluno] = newAluno
                # print(alunos[sala])
                break #finalização do loop
            
            #se caso não for encontrado o aluno na sala
            if not aluno in alunoo:
                print(f"Aluno não econtrado na {sala}")

            break #finalizção do loop
    
    #se a sala não for encontrada
    if not salaPes in sala:
        print("Sala não encontrada!")

#delete - excluir aluno da sala
def Delete():
    salaPes = input("Digite a sala: ")
    for sala, alunoo in alunos.items():
        #verificar se existe a sala pesquisada
        if salaPes in sala:
            aluno = input("Digite o nome do aluno: ")
            #verificar se existe o aluno na sala
            if aluno in alunoo:
                index_aluno = alunos[sala].index(aluno)
                alunos[sala].pop(index_aluno)
                print(alunos[sala])
                break
            #senão for encontrado aluno na sala pesquisada
            if not aluno in alunoo:
                print("Aluno não encontrado nessa sala.")
            
            break
    #se caso a sala não for encontrada
    if not salaPes in sala:
        print("Sala não encontrada")