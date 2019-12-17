#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """get the cities with state_id equal"""
        ret = []
        for k, v in storage.all().keys():
            if k.split(".")[0] == "City":
                if v.state_id == self.id:
                    ret.append(v)
        return ret
