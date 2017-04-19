from bs4 import BeautifulSoup
import tornado.web
from yattag import Doc
from tools import hardg

class Handler(tornado.web.RequestHandler):
    def cr(self):
        self.doc, self.tag, self.text = Doc().tagtext()
        hg = hardg.grabber("res/private/html")
        self.hd = hg.hdict
        del hg
    def clean(self, htmli):
        return BeautifulSoup(htmli, "html.parser").prettify()
    def getGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def get(self):
        self.write(self.clean(self.getGen(self.request.arguments)))
    def postGen(self, arguments):
        return "<html><body><h1>Hello world!</h1></body></html>"
    def post(self):
        self.write(self.clean(self.postGen(self.request.arguments)))
    def getRedirect(self, url):
        self.cr()
        with self.tag("html"):
            with self.tag("head"):
                with self.tag("title"):
                    self.text("Redirecting...")
                self.doc.asis("<meta http-equiv='refresh' content='0; url={0}' />".format(url))
        res = self.doc.getvalue()
        self.cr()
        return res