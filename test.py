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
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'API Test Report', 0, 1, 'C')
        self.ln(5)

def generate_pdf_report(results):
    pdf = TestReportPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 10)
    
    pdf.cell(0, 10, 'Test Results Summary:', 0, 1)
    pdf.ln(5)
    
    for test, result in results.items():
        pdf.cell(0, 10, f'{test}: {result}', 0, 1)
    
    pdf.output("API_Test_Report.pdf")

if __name__ == '__main__':
    unittest.main()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ApiTestCase)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Collect test result summary
    results = {}
    for test_case in suite:
        if test_case is not None:
            test_name = test_case.id().split('.')[-1]  # Extract test method name
            if any(fail[0].id().split('.')[-1] == test_name for fail in result.failures):
                results[test_name] = "FAIL"
            elif any(error[0].id().split('.')[-1] == test_name for error in result.errors):
                results[test_name] = "ERROR"
            else:
                results[test_name] = "PASS"
        else:
            print("Encountered a None test case!")
    
    generate_pdf_report(results)