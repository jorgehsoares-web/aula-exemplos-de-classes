class Animal:
    def __init__(self, nome: str, barulho: str, idade: int = 0):
        self.nome = nome
        self.barulho = barulho
        self.idade = idade

    def fazer_barulho(self):
        print(f"{self.nome} fez {self.barulho}")

    def aniversario(self):
        self.idade += 1
        print(f"O {self.nome} fez {self.idade} anos!")


def main():
    cachorro = Animal("Pastor Alemão", "AU AU!")
    vaca = Animal("Vaca", "MUUUU!")
    gato = Animal("Gato", "MIAU!")

    cachorro.fazer_barulho()
    cachorro.aniversario()
    cachorro.aniversario()

    vaca.fazer_barulho()
    vaca.aniversario()
    vaca.aniversario()

    gato.fazer_barulho()
    gato.aniversario()
    gato.aniversario()


if __name__ == "__main__":
    main()

