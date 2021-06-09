from flask import url_for
from flask_testing import TestCase
import requests_mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.get('http://team_position_api:5000/get_team', text='Manchester Red')
            mocker.posr('http://team_position_api:5000/get_position', text='Center Back')
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Your team is Manchester Red and your playing Center Back', response.data)