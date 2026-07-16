""" 
database/init_db.py
------------------
This module is for 
"""

from database import Base, engine
import models

def init_db():
    Base.metadata.create_all(bind=engine)
    

if __name__ == "__main__":
    init_db()
    print("Database initialized.")