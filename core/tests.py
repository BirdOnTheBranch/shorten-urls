from django.test import TestCase
from .views import HomePageView

# Create your tests here.
class TemplateTestCase(TestCase):
    
    def setUp(self):
        pass

    def ShowTemplate(self):
        self.assertEqual( HomePageView(), home.html)

if __name__ == '__main__':
    unittest.main()