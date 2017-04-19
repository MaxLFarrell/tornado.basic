import tornado.web
import uuid
import json
import base64

class Handler(tornado.web.RequestHandler):
    def post(self):
        nn = self.get_body_argument("name")
        utype = self.get_body_argument("type")
        if utype == "image":
            outf = open("files/" + nn + ".png", "wb")
            outf.write(self.request.files['filearg'][0]['body'])
            outf.close()
            self.write(json.dumps({"image":nn + ".png"}))
            return
        elif utype == "audio":
            outf = open("files/" + nn + ".mp3", "wb")
            outf.write()
            outf.close(self.request.files['filearg'][0]['body'])
            self.write(json.dumps({"image":nn + ".mp3"}))