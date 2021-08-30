class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("saldo {} do titular {}".format(self.saldo, self.titular))

    def deposito(self, valor):
        self.saldo += valor
        print("Novo saldo {} do titular {}".format(self.saldo, self.titular))

    def saque(self, valor):
        self.saldo -= valor
        print("Novo saldo {} do titular {}".format(self.saldo, self.titular))

    def get_numero(self, numero):
        return self.numero

    def get_titular(self, titular):
        return self.titular

    def get_saldo(self, saldo):
        return self.saldo

    def get_limite(self, limite):
        return self.limite








