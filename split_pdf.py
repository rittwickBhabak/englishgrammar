from PyPDF2 import PdfFileWriter, PdfFileReader
import os, PyPDF2
CWD = os.getcwd()

def split_pdf(input_file_path, output_folder):
    inputpdf = PdfFileReader(open(input_file_path, "rb"))

    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    for i in range(inputpdf.numPages):
        output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        with open(f"{os.path.join(output_folder, str(i+1))}.pdf", "wb") as outputStream:
            output.write(outputStream)


if __name__=="__main__":
    files = os.listdir('pdfs')
    for file in files:
        index = int(file.split('.')[0])
        input_file = os.path.join(CWD, 'pdfs', file)
        output_folder = os.path.join(CWD, 'pages', f"chapter-{index}")
        os.mkdir(output_folder)

        split_pdf(input_file, output_folder)

# def count(filename):
#     pdfFileObj = open(os.path.join(os.getcwd(), 'pdfs', filename), 'rb')
#     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#     print(f"{filename}: {pdfReader.numPages}")


# if __name__=="__main__":
#     files = os.listdir('pdfs')
#     for file in files: count(file)
