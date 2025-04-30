import random
def rolar_dados (numero):
    dados = [] # lista de valores dos dados
    for num in range(numero):
        valor = random.randint(1, 6)
        dados.append(valor)
    return dados


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar] # pega o valor do dado
    dados_no_estoque.append(dado) # adiciona o dado na lista
    del dados_rolados[dado_para_guardar] # remove o dado da lista de dados ja rolados
    return [dados_rolados, dados_no_estoque] 
