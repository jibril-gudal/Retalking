import PyPDF2

def read_pdf(file_path):
    pdf_file_obj = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    num_pages = len(pdf_reader.pages)
    text = ''
    for page in range(num_pages):
        page_obj = pdf_reader.pages[page]
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write(text)

file_path = 'paper.pdf'
output_file_path = 'output.txt'

text_content = read_pdf(file_path)
save_text_to_file(text_content, output_file_path)