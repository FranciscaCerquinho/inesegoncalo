from inesegoncalo import model 
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(db.Model, model.Model, model.Base):
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    
    products = relationship('Product', back_populates="category")
    images = relationship('CategoryImage', back_populates="category")
    
    def update_with_dict(self, values):
        if values.get('name') and values['name'] != self.name:
            self.name = values['name']
        self.save()
        return True