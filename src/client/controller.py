import json

from tornado.web import RequestHandler

from dbhandler import SensorHandler


class SensorController(RequestHandler):
    def get(self, *args, **kwargs):
        result, error = None, None
        try:
            sensor_handler = SensorHandler()
            result, sensorlisterr = sensor_handler.list_sensor({})

            if sensorlisterr is not None:
                raise sensorlisterr

            self.set_status(200)
            self.write(json.dumps([sensor.as_dict() for sensor in result]))
        except Exception as err:
            error = err
            self.set_status(500)
            self.write('server side error')
