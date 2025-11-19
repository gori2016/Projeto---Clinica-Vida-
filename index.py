#cria uma lista de pacientes
pacientes = []
#faz um looping até o usuario cancelar o programa digitando a opção 5
while True:
    #Dá ao usuario as opções disponiveis
    print("\n===SISTEMA CLÍNICA VIDA+===")
    print("1 - Cadastrar Paciente")
    print("2 - Ver Estatísticas")
    print("3 - Buscar Pacientes")
    print("4 - Listar todos os pacientes")
    print("5 - Sair")

    #armazena a opção que o usuario escolheu em uma variavel
    opcao = input("Escolha uma opção: ")

    #faz uma condição quando o usuario escolhe a opção 1
    if opcao == "1":
        #armazena nome, idade e telefone em variaveis
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        telefone = input("Digite seu telefone: ")
        #cria um dicionario
        paciente = {"nome": nome, "idade": idade, "telefone": telefone}
        #adiciona os dados que tinha no dicionario e coloca numa lista
        pacientes.append(paciente)
        print("Paciente Cadastrado com sucesso")
    #faz uma condição quando o usuario escolhe a opção 2
    elif opcao == "2":
        #se nenhum paciente estiver cadastrado ele avisará ao usuario
        if len(pacientes) == 0:
            print("Nenhum Paciente Cadastrado ainda")
        else:
            total = len(pacientes)
            media = sum(p["idade"] for p in pacientes) / total
            max_idade = max(pacientes, key=lambda p:p["idade"])
            min_idade = min(pacientes, key=lambda p:p["idade"])
            #exibe todas as informações da lista 
            print(f"Total de Pacientes: {total}")
            print(f"Media de Idade: {media}")
            print(f"Paciente Mais novo: {min_idade}")
            print(f"Paciente Mais velho: {max_idade}")
    #faz uma condição quando o usuario escolhe a opção 3
    elif opcao == "3":
        nome_busca = input("Digite o nome do Paciente: ")
        #por a gente armazena em uma variavel que não encontrou o paciente
        encontrado = False
        #aqui ele faz uma busca pela lista que foi criada
        for x in pacientes:
            if x["nome"].lower() == nome_busca.lower():
                print("\nPACIENTE ENCONTRADO:")
                print(f"Nome: {x['nome']}")
                print(f"Idade: {x['idade']}")
                print(f"Telefone: {x['telefone']}")
                encontrado = True
                break

        if not encontrado:
            print("Paciente Não encontrado")

    elif opcao == "4":
        print(pacientes)

    elif opcao == "5":
        print("Você escolheu Sair Do Sistema")
        break
