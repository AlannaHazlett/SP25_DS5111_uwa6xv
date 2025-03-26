"""
Processes commands
"""
# TEMPLATE
# pylint: disable=too-few-public-methods
class GainerProcess:
    """
    Class to process commands
    """
    def __init__(self, gainer_downloader, gainer_normalizer):
        """
        Initialization method
        """
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        """
        Sends command to appropriate download method
        """
        self.downloader.download()

    def _normalize(self):
        """
        Sends command to appropriate normalize method
        """
        self.normalizer.normalize()

    def _save_to_file(self):
        """
        Sends command to appropriate save with timestamp method
        """
        self.normalizer.save_with_timestamp()

    def process(self):
        """
        Executes the calls
        """
        self._download()
        self._normalize()
        self._save_to_file()
