import random


class Cavaleiro:
    def __init__(self, nome, casa):
        self.nome = nome
        self.casa = casa
        self.vida = 100
        self.forca = 20
    
    def atacar(self, inimigo):
        print(f"⚔️ {self.nome} ataca {inimigo.nome}!")
        success = random.random() < 0.5  # 50% de chance de acerto
        strength = random.random()
        if success:
            dano = int(self.forca * strength)
            print(f"Acertou! Causou {dano} de dano.")
            inimigo.vida -= dano
        else:
            print("Errou o ataque!")
    
    def esta_vivo(self):
        return self.vida > 0
    
    def status(self):
        return f"🛡️ {self.nome} | Vida: {self.vida} | Casa: {self.casa}"

