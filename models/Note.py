from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        return f'<Note {self.title}>'

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}