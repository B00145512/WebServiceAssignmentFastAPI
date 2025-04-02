import unittest, requests

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


if __name__ == '__main__':
    unittest.main()