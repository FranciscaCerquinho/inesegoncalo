from inesegoncalo import model
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer, Text, Boolean
from sqlalchemy.orm import relationship


class Hotel(db.Model, model.Model, model.Base):
    __tablename__ = "hotels"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text)
    phone = Column(Text)
    link = Column(Text)
    images = relationship("HotelImage", back_populates="hotel")

    def update_with_dict(self, values):
        if values["name"] and values["name"] != self.name:
            self.name = values["name"]
        if values["description"] and values["description"] != self.description:
            self.description = values["description"]
        if values["phone"] and values["phone"] != self.phone:
            self.phone = values["phone"]
        if values["link"] and values["link"] != self.link:
            self.link = values["link"]
        self.save()
        return True