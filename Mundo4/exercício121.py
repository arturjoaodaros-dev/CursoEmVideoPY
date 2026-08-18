class Caneta:
    def __init__(self, color="black"):
        self.estado = False
        self.color = color.lower()

    def unclog(self):
        self.estado = True

    def write(self, str):
        from rich import print

        if self.estado:
            print(f"[{self.color}]{str}[/{self.color}]")
        else:
            print([ReferenceError, "did you forgot to unclog the pen?"])

    def newline(*n):
        for i in n:
            print("\n")


c = Caneta("red")
c.unclog()
c.write("ola mundo")
c.newline(9)
c.write("ola mundo")
