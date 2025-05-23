import random
def rolar_dados(numero):
    dados = [] # lista de valores dos dados
    for num in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados


def guardar_dado (dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar] # pega o valor do dado
    dados_no_estoque.append(dado) # adiciona o dado na lista
    del dados_rolados[dado_para_guardar] # remove o dado da lista de dados ja rolados
    return [dados_rolados, dados_no_estoque] 


def remover_dado (dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover]) # adiciona o valor do estoque em dados rolados
    del dados_no_estoque[dado_para_remover] # remove o dado do estoque
    return [dados_rolados, dados_no_estoque]


def calcula_pontos_regra_simples (dados):
    dicio_faces = {}
    for face in range(1, 7): # dá início ao dicionário
        dicio_faces[face] = 0 
    for dado in dados: # soma os dados respectivos
        dicio_faces[dado] += dado
    return dicio_faces


def calcula_pontos_soma (dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma 


def calcula_pontos_sequencia_baixa(dados):
    unicos = []
    for d in dados:
        if d not in unicos:
            unicos.append(d)

    presentes = [False] * 7  # índices 0 a 6
    for valor in unicos:
        if 1 <= valor <= 6:
            presentes[valor] = True

    if presentes[1] and presentes[2] and presentes[3] and presentes[4]:
        return 15
    if presentes[2] and presentes[3] and presentes[4] and presentes[5]:
        return 15
    if presentes[3] and presentes[4] and presentes[5] and presentes[6]:
        return 15

    return 0


def calcula_pontos_sequencia_alta(dados):
    unicos = []
    for d in dados:
        if d not in unicos:
            unicos.append(d)

    presentes = [False] * 7  # índices 0 a 6
    for valor in unicos:
        if 1 <= valor <= 6:
            presentes[valor] = True

    if all([presentes[1], presentes[2], presentes[3], presentes[4], presentes[5]]):
        return 30
    if all([presentes[2], presentes[3], presentes[4], presentes[5], presentes[6]]):
        return 30

    return 0


def calcula_pontos_full_house(dados):
    contagem = {}
    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    if len(contagem) != 2:
        return 0

    quantidades = []
    for quantidade in contagem.values():
        quantidades.append(quantidade)

    if (quantidades[0] == 3 and quantidades[1] == 2) or \
       (quantidades[0] == 2 and quantidades[1] == 3):
        soma = 0
        for valor in dados:
            soma += valor
        return soma

    return 0


def calcula_pontos_quadra(dados):
    contagem = {}
    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    for quantidade in contagem.values():
        if quantidade >= 4:
            soma = 0
            for valor in dados:
                soma += valor
            return soma

    return 0


def calcula_pontos_quina(dados):
    contagem = {}
    for valor in dados:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1

    for quantidade in contagem.values():
        if quantidade >= 5:
            return 50

    return 0


def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }


def faz_jogada(dados, categoria, cartela_de_pontos):
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancados = calcula_pontos_regra_avancada(dados)

    categorias_simples = ["1", "2", "3", "4", "5", "6"]

    if categoria in categorias_simples:
        numero = int(categoria)  
        cartela_de_pontos["regra_simples"][numero] = pontos_simples[numero]
    else:
        cartela_de_pontos["regra_avancada"][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos


def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

