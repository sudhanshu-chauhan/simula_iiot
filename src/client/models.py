import random
import time

from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import (
    Column, ForeignKey,
    String, SmallInteger,
)


Base = declarative_base()


class Machine(Base):
    __tablename__ = 'machines'
    name = Column(String, primary_key=True)

    def __repr__(self):
        return "<Machine (name : {})>".format(
            self.name
        )


class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(SmallInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    machine = Column(String, ForeignKey('machines.name'), nullable=False)
    __tableargs__ = (UniqueConstraint(
        'name', 'machine'))

    def __repr__(self):
        return "<Sensor (name: {}, machine: {})>".format(
            self.name,
            self.machine
        )

    def as_dict(self):
        return {
            'name': getattr(self, 'machine') + ":" + getattr(self, 'name'),
            'value': random.random(),
            'timestamp': time.time()
        }

