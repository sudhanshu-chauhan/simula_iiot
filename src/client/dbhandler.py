import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Machine, Sensor


class MachineHandler():
    def __init__(self):
        self.engine = create_engine(os.environ.get('POSTGRESDB_URL'))

    def create_machine(self, machine_args: dict):
        result, error = None, None
        try:
            with Session(self.engine) as session:
                new_machine = Machine(**machine_args)
                session.add(new_machine)
                session.commit()
                result = new_machine

        except Exception as err:
            error = err
        return result, error

    def list_machine(self, filter_args: dict):
        result, error = None, None
        try:
            with Session(self.engine) as session:
                result = session.query(Machine).filter_by(**filter_args)
        except Exception as err:
            error = err
        return result, error


class SensorHandler():
    def __init__(self):
        self.engine = create_engine(os.environ.get('POSTGRESDB_URL'))

    def create_sensor(self, sensor_args: dict):
        result, error = None, None
        try:
            with Session(self.engine) as session:
                new_sensor = Sensor(**sensor_args)
                session.add(new_sensor)
                session.commit()
                result = new_sensor
        except Exception as err:
            error = err
        return result, error

    def list_sensor(self, filter_args: dict):
        result, error = None, None
        try:
            with Session(self.engine) as session:
                result = session.query(Sensor).filter_by(**filter_args)

        except Exception as err:
            error = err
        return result, error
