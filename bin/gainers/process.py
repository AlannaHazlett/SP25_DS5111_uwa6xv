"""
Module to call process for appropriate gainer.
"""
from abc import ABC, abstractmethod
# PROCESSORS
class GainerProcess(ABC):
    """
    Class to call process for appropriate gainer.
    """
    def __init__(self):
        """
        Initializer method
        """
        #pass

    @abstractmethod
    def normalize(self):
        """
        Method to call to normalize csv
        """
        #pass

    @abstractmethod
    def save_with_timestamp(self):
        """
        Method to call to save raw csv with a timestamp in filename.
        """
       #pass
