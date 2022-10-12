from crypt import methods
from flask import * 
from fpdf import FPDF
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
        return f'file_db(source file name={self.source_file_name}, converted file name={self.converted_file_name})'


@app.route('/')
def start_page():
    return 'Hello!Welcome to project-api'

@app.route('/get-file', methods=['POST'])
def get_file_details():
    # files = request.files.getlist('file[ ]')
    get_file = request.files.getlist('file[ ]')
    for files in get_file:
        get_file_name  = files.filename
        pdf = FPDF()
        pdf.add_page() 
        pdf.set_font("Arial", size = 15) 
        f = open("/home/venkys/Downloads/"+ get_file_name , "r")
        # print("This is f", f)
        db_source_file_name = file_db(source_file_name= "/home/venkys/Downloads/"+ get_file_name)
        db.session.add(db_source_file_name)
        db.session.commit()
        # db.session.commit()
        for x in f: 
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
        pdf.output("/home/venkys/Downloads/" + get_file_name + '_converted.pdf')
        conv_file_name = "/home/venkys/Downloads/" + get_file_name + '_converted.pdf'
        db_converted_file_name = file_db(converted_file_name = conv_file_name)
        db.session.add(db_converted_file_name)
        # display_file_name = file_db.query.order_by(file_db.create_time).all()
        # print("This is it", db_source_file_name,db_converted_file_name)
        db.session.commit()
    return make_response(f"{get_file_name} successfully converted")