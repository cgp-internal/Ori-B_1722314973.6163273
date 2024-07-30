from models.Note import Note
from db import db_session

def get_all_notes():
    session = db_session()
    notes = session.query(Note).all()
    return [note.to_dict() for note in notes]

def get_note(note_id):
    session = db_session()
    note = session.query(Note).get(note_id)
    if note:
        return note.to_dict()
    else:
        return None

def create_note(title, content):
    session = db_session()
    new_note = Note(title, content)
    session.add(new_note)
    session.commit()
    return new_note.to_dict()

def update_note(note_id, title, content):
    session = db_session()
    note = session.query(Note).get(note_id)
    if note:
        note.title = title
        note.content = content
        session.commit()
        return note.to_dict()
    else:
        return None

def delete_note(note_id):
    session = db_session()
    note = session.query(Note).get(note_id)
    if note:
        session.delete(note)
        session.commit()
        return True
    else:
        return False