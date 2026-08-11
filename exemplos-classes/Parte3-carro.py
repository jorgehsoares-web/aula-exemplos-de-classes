class Carro:
    def __init__(self, modelo: str, marca: str, quilometragem: int = 0):
        self.modelo = modelo
        self.marca = marca
        self.combustivel = 100
        self.quilometragem = quilometragem

    def fazer_barulho(self):
        if self.combustivel - 2 >= 0:
            self.combustivel -= 2
            print(f"{self.modelo} está fazendo barulho! \nCombustível: {self.combustivel}")
        else:
            print("Sem combustível para isso!")

    def acelerar(self):
        if self.combustivel - 100 >= 0:
            self.combustivel -= 100
            self.quilometragem += 15
            print(f"{self.modelo} acelerou! \nCombustível: {self.combustivel}")
        else:
            print("Sem combustível para isso!")

    def abastecer(self, quantidade):
        self.combustivel += quantidade

        if self.combustivel > 100:
            self.combustivel = 100

        print(f"{self.modelo} foi abastecido! \nCombustível: {self.combustivel}")

    def painel(self):
        print(f"\n--- PAINEL ---")
        print(f"Modelo: {self.modelo}")
        print(f"Marca: {self.marca}")
        print(f"Combustível: {self.combustivel}")
        print(f"Quilometragem: {self.quilometragem} km")


def main():
    onyx = Carro("Onyx", "Chevrolet")

    onyx.painel()

    onyx.acelerar()
    onyx.acelerar()

    onyx.abastecer(50)

    onyx.painel()


if __name__ == "__main__":
    main()