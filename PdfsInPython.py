from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger
import os

def get_meta(path):
    with open(path,'rb') as f:
        pdf =PdfFileReader(f)
        info = pdf.getDocumentInfo()
        numOP=pdf.getNumPages()
        return "File is "+str(numOP)+" pages long\n "+str(info)

def extract_text(path):
    with open(path,'rb') as f:
        pdf=PdfFileReader(f)
        pageOne=pdf.getPage(1)
        text=pageOne.extractText()
        print(text)
        print(type(text))

def splitPDF(path,output_path):
    with open(path,'rb') as f:
        pdf =PdfFileReader(f)
        for page in range(pdf.getNumPages()):
            writer=PdfFileWriter()
            writer.addPage(pdf.getPage(page))
            with open(f"{output_path}\{page}.pdf","wb") as f_out:
                writer.write(f_out)
def splitByPages(path, output_path,new_name,valid_pages):
    if len(valid_pages)>0:
        with open (path,'rb') as f:
            writer=PdfFileWriter()
            reader=PdfFileReader(path)
            for pageNum in range(reader.getNumPages()):
                if(pageNum in valid_pages):
                    writer.addPage(reader.getPage(pageNum))
            with open(f"{output_path}\{new_name}.pdf",'wb') as f_out:
                writer.write(f_out)
    else:
        print("NO valid pages")

def mergePDF(input_paths,output_path):
     writer=PdfFileWriter()
     for pdf in input_paths:
        reader=PdfFileReader(pdf)
        for pageNum in range(reader.getNumPages()):
            writer.addPage(reader.getPage(pageNum))
     with open(output_path,'wb') as f_out:
         writer.write(f_out)


if __name__=='__main__':
    path=r"C:\Users\Borik\Documents\Max\operatorenEnglisch.pdf"
    mergePDF(["0.pdf","1.pdf"],"merge_out.pdf")