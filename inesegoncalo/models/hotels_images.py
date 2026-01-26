from inesegoncalo import model
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship


class HotelImage(db.Model, model.Model, model.Base):
    __tablename__ = "hotels_images"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True)
    path = Column(Text)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    hotel = relationship("Hotel", back_populates="images")