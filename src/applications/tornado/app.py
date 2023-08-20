from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")


app = Application(
    [
        (r"/", MainHandler),
    ]
)
server = HTTPServer(app)
