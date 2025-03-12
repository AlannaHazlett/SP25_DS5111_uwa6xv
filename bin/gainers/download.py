from abc import ABC, abstractmethod

# DOWNLOADER
class GainerDownload(ABC, url):
    def __init__(self):
        self.url = url

    @abstractmethod
    def download(self):
        pass
