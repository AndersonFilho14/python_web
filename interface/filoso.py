from abc import ABC, abstractmethod

class Filosofo(ABC):
    @abstractmethod
    def frases(self) -> list[str]: pass