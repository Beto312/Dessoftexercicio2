from funcoes import *

def checar_combinacao(combinacao_escolhida, cartela):
    numeros_validos = ['1', '2', '3', '4', '5', '6']
    if combinacao_escolhida in numeros_validos:
        combinacao_escolhida = int(combinacao_escolhida)

    if combinacao_escolhida in cartela['regra_simples']:
        if cartela['regra_simples'][combinacao_escolhida] != -1:
            return 1  # já usada
        else:
            return 2  # válida
    elif combinacao_escolhida in cartela['regra_avancada']:
        if cartela['regra_avancada'][combinacao_escolhida] != -1:
            return 1  # já usada
        else:
            return 2  # válida
    return 0  # inválida

def executar_rodada(cartela, dados_atuais, guardados):
    rerrolagens = 0
    
    while True:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        acao = input()

        if acao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            dados_atuais, guardados = guardar_dado(dados_atuais, guardados, idx)

        elif acao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            dados_atuais, guardados = remover_dado(dados_atuais, guardados, idx)

        elif acao == '3':
            if rerrolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_atuais = rolar_dados(len(dados_atuais))
                rerrolagens += 1

        elif acao == '4':
            imprime_cartela(cartela)

        elif acao == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

        print(f'Dados rolados: {dados_atuais}')
        print(f'Dados guardados: {guardados}')

    todos_dados = dados_atuais + guardados

    print("Digite a combinação desejada:")
    escolha = input()
    validacao = checar_combinacao(escolha, cartela)

    while validacao != 2:
        if validacao == 1:
            print("Essa combinação já foi utilizada.")
        else:
            print("Combinação inválida. Tente novamente.")
        escolha = input()
        validacao = checar_combinacao(escolha, cartela)

    faz_jogada(todos_dados, escolha, cartela)
    return cartela

rolagem_inicial = rolar_dados(5)
dados_guardados = []

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodada_atual = 0

imprime_cartela(cartela)
print(f'Dados rolados: {rolagem_inicial}')
print(f'Dados guardados: {dados_guardados}')

while rodada_atual < 12:
    cartela = executar_rodada(cartela, rolagem_inicial, dados_guardados)
    rodada_atual += 1

    if rodada_atual < 12:
        rolagem_inicial = rolar_dados(5)
        dados_guardados = []
        print(f'Dados rolados: {rolagem_inicial}')
        print(f'Dados guardados: {dados_guardados}')

pontuacao_final = 0
simples_total = 0

for tipo, valores in cartela.items():
    for valor in valores.values():
        pontuacao_final += valor
        if tipo == 'regra_simples':
            simples_total += valor

if simples_total >= 63:
    pontuacao_final += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_final}")
