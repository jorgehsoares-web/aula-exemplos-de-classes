
from datetime import datetime, timedelta


class ContaBancaria:
    def __init__(self, titular: str):
        self.titular = titular
        self.saldo = 0
        self.extrato = []

    def mostrar_informações(self):
        print(f"{self.titular}\nSaldo Atual: {self.saldo}")

    def mostrar_extrato(self):
        for i in self.extrato:
            print(f"{i['data']} > {i['movimento']}")
        print("\n")

    def atualizar_extrato(self, transacao: float):
        self.extrato.append({"data": datetime.now(), "movimento": transacao})

    def adicionar_saldo(self, valor):
        self.saldo += valor
        self.atualizar_extrato(valor)

    def fazer_pix(self, valor):
        if self.saldo - valor < -500:
            print("Limite de saldo negativo excedido!")
        else:
            self.saldo -= valor
            self.atualizar_extrato(-valor)

    def transferir(self, valor, conta_destino):
        if self.saldo - valor < -500:
            print("Transferência bloqueada! Limite de saldo negativo excedido.")
        else:
            print("\nAntes da transferência:")
            self.mostrar_informações()
            conta_destino.mostrar_informações()

            self.saldo -= valor
            self.atualizar_extrato(-valor)

            conta_destino.adicionar_saldo(valor)

            print("\nDepois da transferência:")
            self.mostrar_informações()
            conta_destino.mostrar_informações()


def main():
    minha_conta = ContaBancaria("Gabriel")
    conta_destino = ContaBancaria("João")

    minha_conta.adicionar_saldo(1000)

    minha_conta.transferir(400.2, conta_destino)


if __name__ == "__main__":
    main()
