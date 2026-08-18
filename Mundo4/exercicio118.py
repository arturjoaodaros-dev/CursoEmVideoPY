class Churrasco:
    def __init__(self, title, quant):
        self.titulo = title
        self.quantidade = quant

    def analyse(self):
        from rich import print
        from rich.panel import Panel

        print(
            Panel(
                f"""[white]para esse churrasco é recomendado comprar {str(self.quantidade * 0.4).replace(".", " ").split()[0]},{str(self.quantidade * 0.4).replace(".", " ").split()[1]:.2} KG de carne
preço total da carne: R${str(self.quantidade * 0.4 * 82.4).replace(".", " ").split()[0]},{str(self.quantidade * 0.4 * 82.4).replace(".", " ").split()[1]:.2}
cada participante vai pagar R${str(self.quantidade * 0.4 * 82.4 / self.quantidade).replace(".", " ").split()[0]},{str(self.quantidade * 0.4 * 82.4 / self.quantidade).replace(".", " ").split()[1]:.2}[/white]""",
                title=self.titulo,
                style="red",
            )
        )


Churrasco("churras", 12).analyse()
