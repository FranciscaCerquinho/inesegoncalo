from inesegoncalo import model 
from inesegoncalo.sql_db import db
from sqlalchemy import Column, Integer , Text , Boolean

class FAQ(db.Model ,model.Model,model.Base):
    __tablename__ = 'faq'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    answer = Column(Text)

    def update_with_dict(self,values):
        if values['question'] and values['question'] != self.question:
            self.question = values['question']
        if values['answer'] and values['answer'] != self.answer:
            self.answer = values['answer']
        self.save()
        return True
