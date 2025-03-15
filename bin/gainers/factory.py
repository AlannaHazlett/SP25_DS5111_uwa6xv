"""
Factory Module to direct calls to gainers.
"""
#from abc import ABC, abstractmethod
from yahoo import GainerDownloadYahoo, GainerProcessYahoo
from wsj import GainerDownloadWSJ, GainerProcessWSJ
#import wsj

# FACTORY
# pylint: disable=too-few-public-methods
class GainerFactory:
    """
    Class to trigger wsj.py or yahoo.py
    """
    def __init__(self, choice):
        """
        Initializing method
        """
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """
        Start downloading for applicable gainer
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")

    def get_processor(self):
        """
        Start processing HTML into raw csv for
        applicable gainer.
        """
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        if self.choice == 'wsj':
            return GainerProcessWSJ()
        raise ValueError(f"Unrecognized gainer type: {self.choice}")
