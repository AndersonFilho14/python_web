from abc import ABC, abstractmethod

class Filosofo(ABC):
    @classmethod
    @abstractmethod
    def frases(self) -> list[str]: pass