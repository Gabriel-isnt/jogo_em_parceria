import funcoes_jogo as fn

# classe
# ainda pensando em um nome melhor para essa classe
class Geral:
    def __init__(self, vivo, nome, saude, ataque):
        self.vivo = vivo 
        self.nome = nome
        self.saude = saude
        self.ataque = ataque
        self.inventario = {}

    def esta_vivo(self):
        self.vivo = self.saude > 0

    def atacar(self, dano, pessoa):
        pessoa.saude -= dano

        

# funções que usam instancias
def menu(inventario):
    itens = inventario.copy()

    for opcao, (item, quantidade) in enumerate(itens.items(), start=1):
        print(f'{opcao} -- {item}(x{quantidade})')
    

# o jogo
nome_inimigo = "Dante"

jogador = Geral(True, "nada", 4, 1)
inimigo = Geral(True, nome_inimigo, 4, 1)

jogador.inventario = fn.item_surpresa(3, jogador.inventario)
inimigo.inventario = fn.item_surpresa(3, inimigo.inventario)

print("---------------")
menu(jogador.inventario)
print("---------------")
