class ContaBancaria:
    def __init__(self, nome, saldo):
        self.__id = 56778156
        self.nome = nome
        self._saldo = saldo

    def __str__(self):
        return f"a conta {self.__id} de {self.nome} tem atualmente o saldo de R${self._saldo:,.2f}"

    def depositar(self, v=0):
        self._saldo += v

    def sacar(self, v=0):
        if v < self._saldo * 0.3:
            self._saldo -= v
            print(f"saque DE {v:,.2f} AUTORIZADO PARA A CONTA ID{self.__id}")
        else:
            print(f"saque DE {v:,.2f} NEGADO PARA A CONTA ID{self.__id}")


cnt = ContaBancaria("Artur", 666236984)
print(cnt)
cnt.sacar(999)
