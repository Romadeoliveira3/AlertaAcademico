class Fila:
    """
    Classe que representa uma fila simples.

    Attributes:
        items (list): Uma lista para armazenar os itens na fila.

    Methods:
        enfileirar(item): Adiciona um item ao final da fila.
        desenfileirar(): Remove e retorna o primeiro item da fila.
        esta_vazia(): Verifica se a fila está vazia.
        tamanho(): Retorna o número de itens na fila.
    """

    def __init__(self):
        """Inicializa a fila como uma lista vazia."""
        self.items = []

    def enfileirar(self, item):
        """
        Adiciona um item ao final da fila.

        Args:
            item: O item a ser enfileirado.
        """
        self.items.append(item)

    def desenfileirar(self):
        """
        Remove e retorna o primeiro item da fila.

        Returns:
            O primeiro item da fila, ou None se a fila estiver vazia.
        """
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        """
        Verifica se a fila está vazia.

        Returns:
            True se a fila estiver vazia, False caso contrário.
        """
        return len(self.items) == 0

    def tamanho(self):
        """
        Retorna o número de itens na fila.

        Returns:
            O número de itens na fila.
        """
        return len(self.items)


def gerarNotificacoes(fila):
    """
    Gera notificações a partir de uma fila e exibe na tela.

    Args:
        fila: Uma instância da classe Fila contendo notificações.
    """
    print("Notificações:")
    while not fila.esta_vazia():
        notificacao = fila.desenfileirar()
        print(" -", notificacao)
    print("Todas as notificações foram processadas.")


def adicionarNotificacao(fila, notificacao):
    """
    Adiciona uma notificação à fila.

    Args:
        fila: Uma instância da classe Fila.
        notificacao (str): A notificação a ser adicionada.
    """
    fila.enfileirar(notificacao)
    print("Notificação adicionada:", notificacao)


def removerNotificacao(fila):
    """
    Remove a primeira notificação da fila, se houver.

    Args:
        fila: Uma instância da classe Fila.
    """
    notificacao_removida = fila.desenfileirar()
    if notificacao_removida:
        print("Notificação removida:", notificacao_removida)
    else:
        print("Não há notificações para remover.")


class Aula:
    """
    Classe que representa uma aula em um curso.

    Attributes:
        nome (str): Nome da aula.
        carga_horaria (int): Carga horária total da aula.
        aulas_semana (int): Número de aulas por semana.
        semanas (int): Número de semanas em que a aula ocorre.
        total_aulas (int): Total de aulas no curso.
        aulas_faltadas (int): Número de aulas faltadas.
        percentual_faltas (float): Percentual de faltas em relação ao total de aulas.

    Methods:
        adicionar_falta(): Registra uma falta na aula e verifica a situação de faltas.
        verificar_situacao(): Verifica a situação de faltas e exibe alertas se necessário.
        mostrar_faltas(): Retorna o número de aulas faltadas.
    """
    def __init__(self, nome, carga_horaria, aulas_semana, semanas=None, total_aulas=None, aulas_faltadas=0, percentual_faltas=0):
        """
        Inicializa uma instância da classe Aula.

        Args:
            nome (str): Nome da aula.
            carga_horaria (int): Carga horária total da aula.
            aulas_semana (int): Número de aulas por semana.
            semanas (int, opcional): Número de semanas em que a aula ocorre. Calculado automaticamente se não fornecido.
            total_aulas (int, opcional): Total de aulas no curso. Calculado automaticamente se não fornecido.
            aulas_faltadas (int, opcional): Número de aulas faltadas.
            percentual_faltas (float, opcional): Percentual de faltas em relação ao total de aulas.
        """
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = semanas if semanas is not None else carga_horaria // aulas_semana
        self.total_aulas = total_aulas if total_aulas is not None else self.semanas * aulas_semana
        self.aulas_faltadas = aulas_faltadas
        self.percentual_faltas = percentual_faltas
        self.next = None

    def adicionar_falta(self):
        """Registra uma falta na aula e verifica a situação de faltas."""
        self.aulas_faltadas += 1
        self.verificar_situacao()

    def verificar_situacao(self):
        """Verifica a situação de faltas e exibe alertas se necessário."""
        percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
        if percentual_faltas > 25:
            print(f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas:.2f}%")
        else:
            faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
            print(f"Você pode faltar mais {faltas_restantes:.0f} aulas na disciplina {self.nome} sem ser reprovado por falta.")

    def mostrar_faltas(self):
        """Retorna o número de aulas faltadas."""
        return self.aulas_faltadas


class ListaAulas:
    """
    Classe que representa uma lista encadeada de aulas.

    Attributes:
        head (Aula): O primeiro nó da lista.

    Methods:
        adicionar_aula(nome, carga_horaria, aulas_semana): Adiciona uma nova aula à lista.
        mostrar_aulas(): Exibe as aulas da lista.
        ordenar_por_nome(): Ordena as aulas por nome.
        buscar_aula_por_nome(nome): Busca uma aula pelo nome.
    """
    def __init__(self):
        """Inicializa a lista de aulas como vazia."""
        self.head = None

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        """
        Adiciona uma nova aula à lista.

        Args:
            nome (str): Nome da aula.
            carga_horaria (int): Carga horária total da aula.
            aulas_semana (int): Número de aulas por semana.
        """
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head
        self.head = nova_aula

    def mostrar_aulas(self):
        """Exibe as aulas da lista."""
        aula_atual = self.head
        while aula_atual is not None:
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next

    def ordenar_por_nome(self):
        """
        Ordena as aulas por nome e retorna a lista ordenada.

        Returns:
            Uma lista de instâncias de Aula ordenada por nome.
        """
        aulas = []
        aula_atual = self.head
        while aula_atual is not None:
            aulas.append(aula_atual)
            aula_atual = aula_atual.next
        aulas.sort(key=lambda aula: aula.nome)
        return aulas

    def buscar_aula_por_nome(self, nome):
        """
        Busca uma aula pelo nome e retorna a primeira correspondência encontrada.

        Args:
            nome (str): Nome da aula a ser buscada.

        Returns:
            Uma instância de Aula se encontrada, ou None se não encontrada.
        """
        aula_atual = self.head
        while aula_atual is not None:
            if aula_atual.nome == nome:
                return aula_atual
            aula_atual = aula_atual.next
        return None


class Pilha:
    """
    Classe que representa uma pilha simples.

    Attributes:
        items (list): Uma lista para armazenar os itens na pilha.

    Methods:
        empilhar(item): Adiciona um item ao topo da pilha.
        desempilhar(): Remove e retorna o item do topo da pilha.
        esta_vazia(): Verifica se a pilha está vazia.
    """
    def __init__(self):
        """Inicializa a pilha como uma lista vazia."""
        self.items = []

    def empilhar(self, item):
        """
        Adiciona um item ao topo da pilha.

        Args:
            item: O item a ser empilhado.
        """
        self.items.append(item)

    def desempilhar(self):
        """
        Remove e retorna o item do topo da pilha.

        Returns:
            O item do topo da pilha, ou None se a pilha estiver vazia.
        """
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def esta_vazia(self):
        """
        Verifica se a pilha está vazia.

        Returns:
            True se a pilha estiver vazia, False caso contrário.
        """
        return len(self.items) == 0


def registrarFalta(pilha, acao):
    """
    Registra uma ação na pilha.

    Args:
        pilha: Uma instância da classe Pilha.
        acao (str): A ação a ser registrada na pilha.
    """
    pilha.empilhar(acao)


def desfazerRegistro(pilha):
    """
    Desfaz a última ação registrada na pilha.

    Args:
        pilha: Uma instância da classe Pilha.

    Returns:
        A ação desfeita, ou None se a pilha estiver vazia.
    """
    return pilha.desempilhar()


# Criação da pilha para registro de ações, lista de aulas e fila de notificações.
pilha_de_acoes = Pilha()
lista_de_aulas = ListaAulas()
fila_de_notificacoes = Fila()

while True:
    print("\n1. Adicionar Aula")
    print("2. Mostrar Aulas")
    print("3. Registrar Falta")
    print("4. Desfazer Registro")
    print("5. Adicionar Notificação")
    print("6. Remover Notificação")
    print("7. Gerar Notificações")
    print("8. Ordenar Aulas por Nome")
    print("9. Buscar Aula por Nome")
    print("10. Sair")

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
        nome_aula = input("Digite o nome da aula que deseja buscar: ")
        aula_encontrada = lista_de_aulas.buscar_aula_por_nome(nome_aula)
        if aula_encontrada:
            print(f'Aula encontrada: {aula_encontrada.nome}')
        else:
            print(f'Aula com o nome "{nome_aula}" não encontrada.')
    elif opcao == "10":
        break
    else:
        print("Opção inválida. Escolha novamente.")

