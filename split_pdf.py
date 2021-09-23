from PyPDF2 import PdfFileWriter, PdfFileReader
import os 
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
    split_pdf('16. More about Prepositions.pdf', 'pages')