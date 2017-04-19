from controllers import base

class Handler(base.Handler):
    def getGen(self, args):
        self.cr()
        return self.hd["index"]["index"]