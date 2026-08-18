import random
from abc import *

from rich import *


class Personagem(ABC):
    def __init__(self, nome, vida, *golpes):
        self.nome = nome
        self.vida = vida
        self.cooldown = 0
        self.golpes = golpes

    @abstractmethod
    def Atacar(self, alvo, forca):
        pass

    @abstractmethod
    def Curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida, *golpes):
        super().__init__(nome, vida, *golpes)

    def Curar(self):
        c = random.randint(0, self.vida // 2)
        print(f"você conseguiu um escudo divino e curou {c} pontos de vida")
        self.vida += c
        # diminuir cooldowns apenas para personagens
        for v in globals().values():
            if isinstance(v, Personagem):
                if v.cooldown > 0:
                    v.cooldown -= 1
        # definir o cooldown deste personagem explicitamente
        n = sum(1 for obj in globals().values() if isinstance(obj, Personagem))
        self.cooldown = max(0, n - 1)

    def Atacar(self, alvo, forca):
        if self.cooldown == 0:
            probabilidade = forca / 100
            r = random.random()
            dr = random.randint(0, forca) - 1
            golpe = random.choice(self.golpes)
            if r < probabilidade:
                alvo.vida -= forca
                print(f"você usou o golpe {golpe}")
            elif r < probabilidade + 0.05:
                print(f"o {golpe} acertou de raspão e deu {dr} dano")
                alvo.vida -= dr
            else:
                print(f"você falhou em aplicar o golpe {golpe}")
            for k, v in globals().items():
                if isinstance(v, Personagem):
                    if v.cooldown != 0:
                        v.cooldown -= 1
                    print(f"o cooldown de {k} foi reduzido em -1, atual: {v.cooldown}")
            n = sum(1 for obj in globals().values() if isinstance(obj, Personagem))
            self.cooldown = max(0, n - 1)
        else:
            print("Voê esta em cooldown")


class Mago(Personagem):
    def __init__(self, nome, vida, *golpes):
        super().__init__(nome, vida, *golpes)

    def Curar(self):
        c = random.randint(0, self.vida // 2)
        print(f"você conseguiu um escudo divino e curou {c} pontos de vida")
        self.vida += c
        for v in globals().values():
            if isinstance(v, Personagem):
                if v.cooldown > 0:
                    v.cooldown -= 1
        n = sum(1 for obj in globals().values() if isinstance(obj, Personagem))
        self.cooldown = max(0, n - 1)

    def Atacar(self, alvo, forca):
        if self.cooldown == 0:
            probabilidade = forca / 50
            r = random.random()
            dr = random.randint(0, forca) - 1
            golpe = random.choice(self.golpes)
            if r < probabilidade:
                alvo.vida -= forca
                print(f"você usou o golpe {golpe}")
            elif r < probabilidade + 0.05:
                print(f"o {golpe} acertou de raspão e deu {dr} dano")
                alvo.vida -= dr
            else:
                print(f"você falhou em aplicar o golpe {golpe}")
            for k, v in globals().items():
                if isinstance(v, Personagem):
                    if v.cooldown != 0:
                        v.cooldown -= 1
                    print(f"o cooldown de {k} foi reduzido em -1, atual: {v.cooldown}")
            n = sum(1 for obj in globals().values() if isinstance(obj, Personagem))
            self.cooldown = max(0, n - 1)
        else:
            print("Voê esta em cooldown")


m = Mago("artur", 100, "kwon", "jeb", "cruzado")
g = Guerreiro("thiago", 110, "machadada", "soco", "chute")
m.Atacar(g, 50)
print(m.vida)
m.Atacar(g, 50)
g.Atacar(g, 50)
m.Atacar(g, 50)
g.Atacar(g, 50)
