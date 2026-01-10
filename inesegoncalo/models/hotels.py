from inesegoncalo import model 
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer , Text , Boolean

class Hotel(db.Model ,model.Model,model.Base):
    __tablename__ = 'hotel'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    adress = Column(Text)
    phone = Column(Text)
    email = Column(Text)

    def update_with_dict(self,values):
        if values['name'] and values['name'] != self.name:
            self.name = values['name']
        if values['adress'] and values['adress'] != self.adress:
            self.adress = values['adress']
        if values['phone'] and values['phone'] != self.phone:
            self.phone = values['phone']
        if values['email'] and values['email'] != self.email:
            self.email = values['email']   
        self.save()
        return True
