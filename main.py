# Our sample main file would look like this
import sys
import bin.gainers.factory as gf
#import main_process as pr
import bin.gainers.process as pr
# Make our selection, 'one' choice
choice = sys.argv[1]

# let our factory get select the family of objects for processing
factory = gf.GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

# create our process
runner = pr.GainerProcess(downloader, normalizer)
runner.process()
