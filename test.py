import unittest
import requests
from fpdf import FPDF
import os
import zipfile
from datetime import datetime

class ApiTestCase(unittest.TestCase):
    def test_root_endpoint(self):
        url = "http://localhost:8000/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_singleProd_endpoint(self):
        url = "http://localhost:8000/getSingleProduct/AUTO050"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_getAll_endpoint(self):
        url = "http://localhost:8000/getAll"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_addNew_endpoint(self):
        url = "http://localhost:8000/addNew/AUTO101/TestProduct/30.00/45/CoolProduct"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delOne_endpoint(self):
        url = "http://localhost:8000/deleteOne/AUTO101"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_startWith_endpoint(self):
        url = "http://localhost:8000/startsWith/a"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_paginate_endpoint(self):
        url = "http://localhost:8000/paginate/AUTO005/AUTO012"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_convert_endpoint(self):
        url = "http://localhost:8000/convert/AUTO010"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)


class TestReportPDF(FPDF):
    def header(self):

        self.set_font('Arial', 'B', 16)
        
        self.cell(0, 10, 'Test Report', 0, 1)
        self.ln(5)

def TestReport(test_results, filename="TestCaseReport.pdf"):
    pdf = TestReportPDF()

    pdf.add_page()

    pdf.set_font('Arial', '', 8)
    pdf.ln(5)
    
    for test, result in test_results.items():


        pdf.cell(0, 10, f'{test}: {result}', 0, 1)
    pdf.output(filename)

def createDump():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dumpFolder = f"dumps/{timestamp}_DumpFolder"
    zipFileName = f"dumps/database-{timestamp}.zip"
    uri = "mongodb://root:example@localhost:27017/"


    os.system(f"mongodump --uri={uri} --out={dumpFolder}")
    with zipfile.ZipFile(zipFileName, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolder, filenames in os.walk(dumpFolder):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                zipf.write(filepath, os.path.relpath(filepath, dumpFolder))

    return zipFileName

def createReadme():
    content = """
    FastAPI API Endpoint Reference

    1. /                - Shows all available commands
    2. /getSingleProduct/{product_id}
                       - Returns a single product by ID
    3. /getAll         - Returns all products in the database
    4. /addNew/{product_id}/{name}/{price}/{quantity}/{description}
                       - Adds a new product with given details
    5. /deleteOne/{product_id}
                       - Deletes product with specified ID
    6. /startsWith/{letter}
                       - Lists products starting with specified letter
    7. /panginate/{start_id}/{end_id}
                       - Returns products in a range
    8. /convert/{product_id}
                       - Converts price from USD to EUR

    ===========================================================
    FastAPI Documentation found at: https://fastapi.tiangolo.com
    """.strip()

    with open("README.txt", "w") as file:
        file.write(content)


if __name__ == '__main__':

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ApiTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    test_results = {}
    test_names = [test._testMethodName for test in loader.loadTestsFromTestCase(ApiTestCase)]
    
    for test_name in test_names:
        if test_name in [fail[0]._testMethodName for fail in result.failures]:
            test_results[test_name] = "FAIL"
        elif test_name in [error[0]._testMethodName for error in result.errors]:
            test_results[test_name] = "ERROR"
        else:
            test_results[test_name] = "PASS"
    
    TestReport(test_results)
    createDump()
    createReadme()