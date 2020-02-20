from django.http import HttpRequest
from django.test import TestCase

from .views import home_page

# Create your tests here.
class HomePageList(TestCase):
    def test_home_page(self):
        request = HttpRequest()
        response = home_page(request)

        with open('lists/templates/lists/home.html') as f:
            expected_content = f.read()
        self.assertEqual(response.content.decode(), expected_content)
