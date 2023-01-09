from django.test import TestCase
from django.urls import reverse

from pages.models import Pages


# Create your tests here.
class SimpleTests(TestCase):
    # def test_home_page_status_code(self):
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_about_page_status_code(self):
    #     response = self.client.get('/about/')
    #     self.assertEqual(response.status_code, 200)

    def setUp(self):
        Pages.objects.create(text='just a test')

    def test_text_content(self):
        post = Pages.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):  # new
    def setUp(self):
        Pages.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'pages/home.html')
