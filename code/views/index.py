from controllers import base

class Handler(base.Handler):
    def getGen(self, args):
        self.cr()
        html = "<html>"
        html += self.hd["shared"]["head"].replace("#TITLE", "Home")
        html += "<body>"
        html += self.hd["shared"]["nav"]
        html += self.hd["index"]["index"]
        html += self.hd["shared"]["footer"]
        html += "</body></html>"
        return html