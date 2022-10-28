from fpdf import FPDF
import os

def convert_to_pdf(get_file_name):
    pdf = FPDF()
    pdf.add_page() 
    pdf.set_font("Arial", size = 15)
    f = open(os.path.expanduser('~')  +'/Downloads/' + get_file_name , "r")
    for x in f: 
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
        pdf.output(os.path.expanduser('~') + '/' +get_file_name + '_converted.pdf')