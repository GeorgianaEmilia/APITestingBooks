from books.requests.api_clients import *
from random import randint

class TestApiClient:
    nr=randint(1,9999999)
    clientName='NICO'
    clientEmail=f'email_valid{nr}@gmail.com'

    def setup_method(self):
        self.response=login(self.clientName,self.clientEmail)

    def test_login_200(self):
        assert self.response.status_code==201,'status code is not ok'

    def test_login_409(self):
        self.response=login(self.clientName, self.clientEmail)
        assert self.response.status_code==409, 'status code is not ok'
        assert self.response.json()['error']=='API client already registered. Try a different email.'

    def test_invalid_email(self):
        self.response=login('NICO','abc')
        assert self.response.status_code==400,'status code is not ok'
        assert self.response.json()['error']=='Invalid or missing client email.','INVALID EMAIL ERROR MSG IS NOT OK'