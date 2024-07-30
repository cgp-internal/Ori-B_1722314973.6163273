import os
import sqlite3
from models.Note import Note
from app_config import DB_PATH

def create_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY, content TEXT)''')
    
    conn.commit()
    conn.close()

def insert_sample_data():
    notes = [
        {'content': 'Note 1 content'},
        {'content': 'Note 2 content'},
        {'content': 'Note 3 content'}
    ]
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.executemany('INSERT INTO notes (content) VALUES (:content)', notes)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    if not os.path.exists(DB_PATH):
        create_db()
        insert_sample_data()