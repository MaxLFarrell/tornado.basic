import tornado.ioloop
import tornado.web
import views
from views import *
import importlib

def make_app():
    handlers = []
    for mod in views.__all__:
        if (not (mod in ["__init__","__pycache__"])):
            if (mod == "index"):
                handlers.append((r"/", eval(mod + ".Handler")))
            else:
                handlers.append((r"/" + mod, eval(mod + ".Handler")))
    handlers.append((r"/static/(.*)", tornado.web.StaticFileHandler, {'path':'res/public'}))
    t =  tornado.web.Application(handlers)
    return t

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()