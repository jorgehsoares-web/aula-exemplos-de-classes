class Aluno:
    GABARITOS = [
        ("a", "b", "a", "d", "c"),
        ("b", "c", "d", "a", "b"),
        ("c", "a", "b", "a", "c")
    ]

    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.historico_notas = []

    def fazer_prova(self, respostas: tuple[str, ...], gabarito):
        nota = 0

        for resposta, correta in zip(respostas, gabarito):
            if resposta == correta:
                nota += 2

        self.historico_notas.append(nota)

    def calcular_media(self):
        if len(self.historico_notas) == 0:
            return 0

        return sum(self.historico_notas) / len(self.historico_notas)

    def ver_boletim(self):
        media = self.calcular_media()

        if media >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"Aluno(a): {self.nome} {self.sobrenome}")
        print(f"Notas: {self.historico_notas}")
        print(f"Média final: {media}")
        print(f"Situação: {situacao}")


def main():
    arthur = Aluno("Arthur José", "Figueiredo", 18)

    arthur.fazer_prova(("a", "b", "a", "d", "d"), Aluno.GABARITOS[0])
    arthur.fazer_prova(("b", "c", "d", "a", "b"), Aluno.GABARITOS[1])
    arthur.fazer_prova(("c", "a", "b", "c", "d"), Aluno.GABARITOS[2])

    arthur.ver_boletim()


if __name__ == "__main__":
    main()