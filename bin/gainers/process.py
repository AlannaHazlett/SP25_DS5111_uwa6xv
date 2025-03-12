from abc import ABC, abstractmethod
# PROCESSORS 
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass
