#extract text from a PDF

from PyPDF2 import PdfReader
import sys
import logging

logging.basicConfig(filename="logging.txt", level=logging.INFO)

def pdf_export():
    reader = PdfReader(sys.argv[1])


    for page_id , page in enumerate(reader.pages) :
        print("Page No : ",page_id)
        page_content = page.extract_text()
        print(page_content)    
        print("\n----------------------------------")
    

try:
    logging.info("Starting App")
    print("""
    Project : PDF Translater Console App
    Author  : MQuel
    Version : v1.0
    License : 2023 - 2030
    """)
    if len(sys.argv) < 5:
        
        print(" PDF_Translater_Project --filePath --langFrom --langTo --NewFileName")
    

    else:
        _filePath = sys.argv[1]
        _from = sys.argv[2]
        _to = sys.argv[3]
        _newFileName = sys.argv[4]
        print("File:", _filePath)
        print("Translate From:",_from)
        print("Translate To:",_to)
        print("New File:",_newFileName)
        


    input("Press any key to get the output!")
    pass
except Exception as e:
    logging.error("Error : %s",e)