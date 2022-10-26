from crypt import methods
from flask import * 
from fpdf import FPDF
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid


app = Flask(__name__)
# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///file.db"
# Initializing the database
db = SQLAlchemy(app)


# Create a model
class file_db(db.Model):
    source_file_name = db.Column(db.String)
    create_time = db.Column(db.DateTime, default=datetime.utcnow, primary_key = True)
    converted_file_name = db.Column(db.String)
    
    def __repr__(self) -> str:
        return f'file_db(source file name={self.source_file_name}, converted file name={self.converted_file_name}, created file date={self.create_time})'

@app.route('/')
def start_page():
    return 'Hello!Welcome to project-api'

@app.route('/get-file', methods=['GET','POST'])
def get_file_details():
    if request.method == 'POST':
        get_file = request.files.getlist('file[ ]')
        for files in get_file:
            get_file_name  = files.filename
            pdf = FPDF()
            pdf.add_page() 
            pdf.set_font("Arial", size = 15) 
            f = open("/home/venkys/Downloads/"+ get_file_name , "r")
            db_source_file_name = file_db(source_file_name= "/home/venkys/Downloads/"+ get_file_name)
            db.session.add(db_source_file_name)
            db.session.commit()
            for x in f: 
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
            pdf.output("/home/venkys/Downloads/" + get_file_name + '_converted.pdf')
            conv_file_name = "/home/venkys/Downloads/" + get_file_name + '_converted.pdf'
            db_converted_file_name = file_db(converted_file_name = conv_file_name)
            db.session.add(db_converted_file_name)
            db.session.commit()
            print()
    return make_response(f"{get_file_name} successfully converted")

if __name__ == '__main__':
    app.run(debug=True)

# Put valdations - only txt files , try exception, uuid, get a cofig.yaml, __init__ for db, oops classes 