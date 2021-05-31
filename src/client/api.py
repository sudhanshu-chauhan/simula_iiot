from tornado.ioloop import IOLoop
from tornado.web import Application

from controller import SensorController


class EdgeAPI(Application):
    def __init__(self):
        handlers = [
            (r'/sensor/list', SensorController)
        ]
        Application.__init__(self, handlers)


def main():
    api_instance = EdgeAPI()
    api_instance.listen(8001, address='0.0.0.0')
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
