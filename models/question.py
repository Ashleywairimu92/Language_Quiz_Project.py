from sqlalchemy import Column, Integer, String
from database import Base

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable=False)
    correct_answer = Column(String, nullable=False)
    options = Column(String)  

    def __repr__(self):
        return f"<Question(question={self.question_text})>"
