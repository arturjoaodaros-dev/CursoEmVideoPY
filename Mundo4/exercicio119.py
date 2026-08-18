class Livro:
    def __init__(self, title, page=0):
        self.title = title
        self.currentpage = 0
        self.page = page

    def regredir_pagina(self, q):
        from time import sleep

        if self.currentpage == 0:
            print(f"Você está começando o livro [blue]{self.title}[/blue]")
        if self.currentpage <= self.page:
            for i in range(q):
                if self.currentpage >= 1:
                    print(f"PG{self.currentpage}>", end="", flush=True)
                    self.currentpage -= 1
                    sleep(0.1)
            print(f"paginas regredidas, agora você esta na pagina {self.currentpage}")

    def avançar_pagina(self, q):
        from time import sleep

        if self.page == 0:
            print(f"Você está começando o livro [blue]{self.title}[/blue]")
            for i in range(q):
                if self.currentpage < self.page:
                    print(f"PG{self.currentpage}>", end="", flush=True)
                    self.currentpage += 1
                    sleep(0.1)
            print(f"paginas avançadas, agora você esta na pagina {self.currentpage}")
        if self.currentpage <= self.page:
            for i in range(q):
                if self.currentpage < self.page:
                    print(f"PG{self.currentpage}>", end="", flush=True)
                    self.currentpage += 1
                    sleep(0.1)
            print(f"paginas avançadas, agora você esta na pagina {self.currentpage}")
        else:
            print(f"infelizmente, você já acabou o livro [blue]{self.title}[/blue]")


l = Livro("As cronicas de fiorella", 9)
l.avançar_pagina(10)
l.regredir_pagina(11)
