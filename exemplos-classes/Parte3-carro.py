class Carro:
    def __init__(self, modelo : str, marca : str):
        self.modelo = modelo
        self.marca = marca
        self.combustivel = 10000000
    
    def fazer_barulho(self):
        if self.combustivel - 2 >= 0:
           self.combustivel -= 2
           print(f"{self.modelo} está fazendo barulho! \nCombustível: {self.combustivel}")
        else:
           print("Sem combustível para isso!")
    
    def acelerar(self):
        if self.combustivel - 100 >= 0:
           self.combustivel -= 100
           print(f"{self.modelo} acelerou! \nCombustível: {self.combustivel}")
        else:
           print("Sem combustível para isso!")

def main():
    onyx = Carro("Onyx", "Chevrolet")
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()
    onyx.acelerar()

if __name__ == "__main__":
    main()