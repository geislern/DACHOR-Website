from django.test import Client, TestCase
from django.urls import reverse


class WebsiteTests(TestCase):
    """
    Test the website component
    """

    VIEWS = [
        'homepage', 'about', 'contact', 'events', 'impress', 'privacy'
    ]

    def testViews(self):
        """
        Test whether opening a view returns an error
        """
        client = Client()

        for v in self.VIEWS:
            response = client.get(reverse('website:'+v))
            self.assertEqual(response.status_code, 200,
                              f"Loading view '{v}' produced error {response.status_code}")
