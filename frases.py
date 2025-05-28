from interface.filoso import Filosofo

class Estoico(Filosofo):
    mensagens = ["O homem que sofre antes de ser necessário, sofre mais que o necessário.",
         "Nada de desgosto, nem de desânimo; se acabas de fracassar, recomeça.",
         "A nossa vida é aquilo que os nossos pensamentos fizerem dela."
        ]
    @classmethod
    def frases(cls) -> list[str]:
        return cls.mensagens
