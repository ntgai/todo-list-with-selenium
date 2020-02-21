from django.http import HttpRequest
from django.test import TestCase
from django.template.loader import render_to_string

from .views import home_page

# Create your tests here.
class HomePageList(TestCase):
    def test_home_page_is_about_todo_lists(self):
        request = HttpRequest()
        response = home_page(request)

        # self.assertEqual(response.templates[0].name, 'home.html')
        expected_content = render_to_string('lists/home.html')
        self.assertEqual(response.content.decode(), expected_content)

    def test_home_page_can_remember_post_requests(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "A new item"

        response = home_page(request)
        self.assertIn('A new item', response.content.decode())
        expected_content = render_to_string('lists/home.html', {'new_item_text': 'A new item'})
        self.assertEqual(response.content.decode(), expected_content)
