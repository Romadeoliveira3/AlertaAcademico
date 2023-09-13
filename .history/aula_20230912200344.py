while True:
    print("\n1. Adicionar Aula")
    print("2. Mostrar Aulas")
    print("3. Registrar Falta")
    print("4. Desfazer Registro")
    print("5. Adicionar Notificação")
    print("6. Remover Notificação")
    print("7. Gerar Notificações")
    print("8. Ordenar Aulas por Nome")  # Adicione uma nova opção de ordenação
    print("9. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome da aula: ")
        carga_horaria = int(input("Carga horária: "))
        aulas_semana = int(input("Aulas por semana: "))
        lista_de_aulas.adicionar_aula(nome, carga_horaria, aulas_semana)
    elif opcao == "2":
        lista_de_aulas.mostrar_aulas()
    elif opcao == "3":
        aula_escolhida = input("Digite o nome da aula para registrar a falta: ")
        registrarFalta(pilha_de_acoes, f"Registro de falta em {aula_escolhida}")
        aula_encontrada = lista_de_aulas.head
        while aula_encontrada is not None:
            if aula_encontrada.nome == aula_escolhida:
                aula_encontrada.adicionar_falta()
                break
            aula_encontrada = aula_encontrada.next
    elif opcao == "4":
        acao_desfeita = desfazerRegistro(pilha_de_acoes)
        if acao_desfeita:
            print("Ação desfeita:", acao_desfeita)
        else:
            print("Não há ações para desfazer.")
    elif opcao == "5":
        notificacao = input("Digite a notificação: ")
        adicionarNotificacao(fila_de_notificacoes, notificacao)
    elif opcao == "6":
        removerNotificacao(fila_de_notificacoes)
    elif opcao == "7":
        gerarNotificacoes(fila_de_notificacoes)
    elif opcao == "8":
        aulas_ordenadas = lista_de_aulas.ordenar_por_nome()
        print("Aulas ordenadas por nome:")
        for aula in aulas_ordenadas:
            print(f'Nome da aula: {aula.nome}, Faltas: {aula.mostrar_faltas()}')
    elif opcao == "9":
        break
    else:
        print("Opção inválida. Escolha novamente.")