import random as rd 


def erro(msg):  # usado pelo programador para avisar algo inválido ao usuário
    print(f"\033[91m{msg}\033[0m")


def item_surpresa(quantidade, inventario):
    # rolo de camera = revela para você se a bala é de chumbinho ou de verdade na sua vez
    # esparadrapo = recupera uma vida
    # amarrador = adversário perde a vez
    # faca = tiro vale por 2  (na vida e no carregador)
    # lápis = altera a munição da arma 
    itens = ('rolo de camera', 'esparadrapo', 'amarrador', 'faca', 'lápis')

    pessoa = inventario
    
    for _ in range(0, quantidade):  # para colocar os itens no inventário
       pessoa.append(rd.choice(itens))
        
    return pessoa

def nome():
    return str(input("digite o seu nome: "))[:7]  # só aceita 7 letras isso ai

def altera_municao():
    pass

