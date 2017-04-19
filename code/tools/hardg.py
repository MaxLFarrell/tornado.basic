import os
class grabber:
    def __init__(self, htmldir):
        hdict = {}
        for folder in os.listdir(htmldir):
            hdict[folder] = {}
            for hpage in os.listdir("{0}/{1}".format(htmldir, folder)):
                with open("{0}/{1}/{2}".format(htmldir, folder, hpage), "r") as tmpp:
                    tmpn = hpage.split(".")[0]
                    hdict[folder][tmpn] = tmpp.read()
        self.hdict = hdict