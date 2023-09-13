class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

def gerarNotificacoes(fila):
    print("Notificações:")
    while not fila.esta_vazia():
        notificacao = fila.desenfileirar()
        print(" -", notificacao)
    print("Todas as notificações foram processadas.")

def adicionarNotificacao(fila, notificacao):
    fila.enfileirar(notificacao)
    print("Notificação adicionada:", notificacao)

def removerNotificacao(fila):
    notificacao_removida = fila.desenfileirar()
    if notificacao_removida:
        print("Notificação removida:", notificacao_removida)
    else:
        print("Não há notificações para remover.")


class Aula:
    def __init__(self, nome, carga_horaria, aulas_semana, semanas=None, total_aulas=None, aulas_faltadas=0, percentual_faltas=0):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.aulas_semana = aulas_semana
        self.semanas = semanas if semanas is not None else carga_horaria // aulas_semana
        self.total_aulas = total_aulas if total_aulas is not None else self.semanas * aulas_semana
        self.aulas_faltadas = aulas_faltadas
        self.percentual_faltas = percentual_faltas
        self.next = None  

    def adicionar_falta(self):
        self.aulas_faltadas += 1
        self.verificar_situacao()

    def verificar_situacao(self):
        percentual_faltas = (self.aulas_faltadas / self.total_aulas) * 100
        if percentual_faltas > 25:
            print(f"Alerta! Você ultrapassou o limite de faltas na disciplina {self.nome}. Percentual de faltas: {percentual_faltas:.2f}%")
        else:
            faltas_restantes = (self.total_aulas * 0.25) - self.aulas_faltadas
            print(f"Você pode faltar mais {faltas_restantes:.0f} aulas na disciplina {self.nome} sem ser reprovado por falta.")

    def mostrar_faltas(self):
        return self.aulas_faltadas


class ListaAulas:
    def __init__(self):
        self.head = None 

    def adicionar_aula(self, nome, carga_horaria, aulas_semana):
        nova_aula = Aula(nome, carga_horaria, aulas_semana)
        nova_aula.next = self.head  
        self.head = nova_aula  

    def mostrar_aulas(self):
        aula_atual = self.head  
        while aula_atual is not None:  
            print(f'Nome da aula: {aula_atual.nome}, Faltas: {aula_atual.mostrar_faltas()}')
            aula_atual = aula_atual.next 


class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0

def registrarFalta(pilha, acao):
    pilha.empilhar(acao)

def desfazerRegistro(pilha):
    return pilha.desempilhar()

# Criação da pilha
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
    print("8. Sair")
    
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
        break
    else:
        print("Opção inválida. Escolha novamente.")
