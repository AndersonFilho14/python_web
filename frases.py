from interface.filoso import Filosofo

class Estoico(Filosofo):
    mensagens = ["O homem que sofre antes de ser necessário, sofre mais que o necessário.",
         "Nada de desgosto, nem de desânimo; se acabas de fracassar, recomeça.",
         "A nossa vida é aquilo que os nossos pensamentos fizerem dela."
        ]
    @classmethod
    def get_frases(cls) -> list[str]:
        return cls.mensagens

class Pessoa():
    def __init__(self, nome:str, idade:int, sexo):
        self.nome = nome
        self.idade =idade
        self.sexo = sexo
        pass
