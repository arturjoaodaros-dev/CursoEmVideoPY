class Gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.games = []

    def Ficha(self, show=False):
        if show:
            print(
                f"o nome do usuário é {self.name}, seu nick é {self.nick} e seu(s) jogos favoritos são {self.games}"
            )

    def add_game(self, *str):
        for i in str:
            self.games.append(i)


gamer = Gamer("Artur", "finefire7s")
gamer.add_game("RL", "tuff")
gamer.Ficha(True)
