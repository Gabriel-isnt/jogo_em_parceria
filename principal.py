import funcoes_jogo as fn
import historia as cena

# ainda pensando em um nome melhor para essa classe
class Geral:
    def __init__(self, vivo, nome, saude, ataque):
        self.vivo = vivo 
        self.nome = nome
        self.saude = saude
        self.ataque = ataque
        self.inventario = []

    def esta_vivo(self):
        if self.saude <= 0:
            self.vivo = False
        
        self.vivo = True

    
# o jogo

cena.historia_inicial()
cena.explicacao()

nome_player = fn.nome()
nome_inimigo = "Dante"

jogador = Geral(True, nome_player, 4, 1)
inimigo = Geral(True, nome_inimigo, 4, 1)

jogador.inventario = fn.item_surpresa(3, jogador.inventario)
inimigo.inventario = fn.item_surpresa(3, inimigo.inventario)

