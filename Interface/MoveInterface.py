from abc import ABC, abstractmethod

class MoveInterface(ABC):
    @abstractmethod
    def move(self) -> None:
        pass
    
    
    