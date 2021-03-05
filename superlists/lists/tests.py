
from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):
    def test_home_page_returns_the_correct_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')

        self.assertTemplateUsed(response, 'home.html')
