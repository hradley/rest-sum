import app
import unittest


class TotalTestCase(unittest.TestCase):

    def setUp(self):
        test_app = app.create_app()
        test_app.testing = True
        self.app = test_app.test_client()

    def test_get_total(self):
        response = self.app.get('/total')
        result = response.json['total']
        self.assertEqual(50000005000000, result)
        self.assertEqual(200, response.status_code)

    def test_post_total(self):
        response = self.app.post('/total', json={'numbers': list(range(10000001))})
        result = response.json['total']
        self.assertEqual(50000005000000, result)
        self.assertEqual(200, response.status_code)

    def test_wrong_endpoint(self):
        response = self.app.get('/tota')
        self.assertEqual(404, response.status_code)

    def test_post_wrong_input(self):
        response = self.app.post('/total', json={'nums': '1'})
        self.assertEqual(400, response.status_code)

    def test_post_no_input(self):
        response = self.app.post('/total', json={})
        self.assertEqual(400, response.status_code)
