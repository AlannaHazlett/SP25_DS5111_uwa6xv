"""
Module calls to the appropriate gainer script to download the gainers.
"""
from abc import ABC, abstractmethod

# DOWNLOADER
# pylint: disable=too-few-public-methods
class GainerDownload(ABC):#, url):
    """
    This class calls to the appropriate gainer script to download the gainers.
    """

    def __init__(self):
        """
        Initializer function
        """
        #self.url = url
        #pass

    @abstractmethod
    def download(self):
        """
        Creation of download function
        """
        #pass
