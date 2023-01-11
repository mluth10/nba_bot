from abc import ABC, abstractmethod

class GameOccurrence(ABC):
    @abstractmethod
    def check(board):
        pass