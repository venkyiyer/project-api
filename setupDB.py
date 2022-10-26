from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


# Add database

# Initializing the database
db = SQLAlchemy()
# db.create_all()

#Base = declarative_base()
#engine = create_engine("sqlite:///file_info.db")
#Base.metadata.create_all(engine)

class file_db(db.Model):
    __tablename__ = 'files'
    source_file_name = db.Column(String(350))
    converted_file_name = db.Column(String(500))
    time_stamp = db.Column(DateTime, default=datetime.utcnow, primary_key = True)

    # engine = create_engine("sqlite:///file.db")
    # Base.metadata.create_all(engine)

    def __repr__(self) -> str:
        rep = 'File_data(' + self.source_file_name + "," + self.converted_file_name + "," + self.time_stamp + ')'
        return rep