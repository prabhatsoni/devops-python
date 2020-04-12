'''A module for testing'''
import unittest
from app import APP

class Tests(unittest.TestCase):
	'''Basic tests for the application'''
	def setUp(self):
		'''Create a test client for the app'''
		self.app = APP.test_client()
		
	def test_200(self):
		res = self.app.get('/')
		assert res.status == '200 OK'
	
	def test_404(self):
		res = self.app.get('/null')
		assert res.status == '404 NOT FOUND'

if __name__ == "__main__":
	unittest.main()