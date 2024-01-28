import random as rd 
        
def erro(msg):  # usado pelo programador para avisar algo inválido ao usuário
    print(f"\033[91m{msg}\033[0m")

def nome():
    return str(input("digite o seu nome: "))[:7]  # só aceita 7 letras isso ai

def item_surpresa(quantidade, inventario):
    # rolo de camera = revela para você se a bala é de chumbinho ou de verdade na sua vez
    # esparadrapo = recupera uma vida
    # amarrador = adversário perde a vez
    # faca = tiro vale por 2  (na vida e no carregador)
    # lápis = altera a munição da arma 
    itens = ('rolo de camera', 'esparadrapo', 'amarrador', 'faca', 'lápis')

    # eu crio o dicionário para ele receber os valores antigos
    # para ser adicionado mais coisa no primeiro for
    item_usuário = inventario.copy()

    # escolhe os itens aleatoriamente
    itens_escolhidos = []    

    for _ in range(0, quantidade):
        itens_escolhidos.append(rd.choice(itens))

    # adicionando item e quantidade automaticamente
    for item in itens_escolhidos:
        if item in item_usuário:
            item_usuário[item] += 1
        
        else:
            # pq ai já cria com um valor normal
            item_usuário[item] = 1

    # fim da função
    return item_usuário

