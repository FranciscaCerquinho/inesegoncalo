from inesegoncalo import model
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer, Text


class HotelReservation(db.Model, model.Model, model.Base):
    __tablename__ = "hotel_reservations"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    guest_names = Column(Text, nullable=False)
    num_rooms = Column(Integer, nullable=False)
    num_people = Column(Integer, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
