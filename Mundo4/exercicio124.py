import asyncio
from abc import *


class BebidaQuente(ABC):
    def __init__(self, temperatura, fervido=False, misturado=False, preparado=False):
        self.temperatura = temperatura
        self.fervido = fervido
        self.misturado = misturado
        self.prepardo = preparado

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

    async def espera(self):
        await asyncio.sleep(100)
        self.fervido = False

    def FerverAgua(self):
        from time import sleep

        from rich import print
        from tqdm import tqdm

        print(f"[blue]Fervendo a água a {self.temperatura}°c[/blue]")
        for i in tqdm(range(50)):
            sleep(5 / self.temperatura)
        self.fervido = True
        asyncio.create_task(self.espera())

    def Preparar(self):
        from time import sleep

        from rich import print
        from tqdm import tqdm

        print("[red]Preparando a sua bebida[/red]")
        for i in tqdm(range(50)):
            sleep(0.05)
        self.preparado = True


class Cafe(BebidaQuente):
    def __init__(self, temperatura, ml, fervido, misturado, preparado):
        super().__init__(temperatura, fervido, misturado, preparado)
        self.ml = ml
        self.fervido = fervido
        self.misturado = misturado
        self.prepardo = preparado

    def misturar(self):
        from time import sleep

        from rich import print
        from tqdm import tqdm

        print("[brown]misturando o pó de cafe[/brown]")
        for i in tqdm(range(50)):
            sleep(5 / self.ml)
        self.misturado = True

    def servir(self):
        if self.fervido and self.prepardo and self.misturado:
            print("[bold yellow]seu café foi servido com sucesso[/bold yellow]")
        else:
            print("você esqueceu de alguma etapa")


class Chá(BebidaQuente):
    def __init__(
        self, temperatura, ml, fervido=False, misturado=False, preparado=False
    ):
        super().__init__(temperatura, fervido, misturado, preparado)
        self.ml = ml
        self.fervido = fervido
        self.misturado = misturado
        self.prepardo = preparado

    def misturar(self):
        from time import sleep

        from rich import print
        from tqdm import tqdm

        if self.fervido:
            print("[brown]colocando o sachê na agua fervendo[/brown]")
        else:
            raise NotImplementedError("Ferva a agua primeiro")
        for i in tqdm(range(50)):
            sleep(5 / self.ml)
        self.misturado = True

    def servir(self):
        if self.fervido and self.prepardo and self.misturado:
            print("[bold yellow]seu chá foi servido com sucesso[/bold yellow]")
        else:
            print("você esqueceu de alguma etapa")


class Leite(BebidaQuente):
    def __init__(self, temperatura, ml, fervido, misturado, preparado):
        super().__init__(temperatura, fervido, misturado, preparado)
        self.ml = ml
        self.fervido = fervido
        self.misturado = misturado
        self.prepardo = preparado

    def misturar(self):
        from time import sleep

        from rich import print
        from tqdm import tqdm

        print("[brown]misturando o pó de cafe[/brown]")
        for i in tqdm(range(50)):
            sleep(5 / self.ml)
        self.misturado = True

    def servir(self):
        if self.fervido and self.prepardo and self.misturado:
            print("[bold yellow]seu leite foi servido com sucesso[/bold yellow]")
        else:
            print("você esqueceu de alguma etapa")


async def main():
    b = Chá(200, 100)
    b.FerverAgua()
    await asyncio.sleep(101)
    b.misturar()


asyncio.run(main())
