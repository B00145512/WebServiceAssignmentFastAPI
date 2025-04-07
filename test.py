import unittest
import requests
from fpdf import FPDF

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

    def test_panginate_endpoint(self):
        url = "http://localhost:8000/panginate/AUTO005/AUTO012"
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