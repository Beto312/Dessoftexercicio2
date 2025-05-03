import random
def rolar_dados (numero):
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