class Hero:
    def __init__(self, nome, idade, classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe

    def atacar(self):
        tipo_ataque = ""
        if self.classe == "mago":
            tipo_ataque = "canalizou mana e lançou uma bola de fogo!"
        elif self.classe == "guerreiro":
            tipo_ataque = "deu um golpe no chão com o seu machado!"
        elif self.classe == "caçador":
            tipo_ataque = "puxou seu arco e atirou uma flecha precisa!"
        elif self.classe == "ninja":
            tipo_ataque = "jogou um shuriken e desapareceu nas sombras"

        print(f"O {self.classe} {self.nome} {tipo_ataque}")

nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
classe = input("Digite a classe do herói (mago, guerreiro, caçador, ninja): ").lower()

hero1 = Hero(nome=nome, idade=idade, classe=classe)
hero1.atacar()
