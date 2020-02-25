from django.test import TestCase, Client
from .models import Link
from django.contrib.auth import get_user_model


class ViewLinks(TestCase):
    def setUp(self):
        """ User for register and create test"""
        UserModel = get_user_model()
        self.user = UserModel.objects.create_user('wane', 'wane@a.com', 'wane')
        #Create active user 


    def test_for_invalid_input_renders_home_template(self):
        """ Invalids users in template """
        response = self.client.post('/', data={'url': '456367'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/home.html')
        #if Http returns code 200 and client in "/" returns template home.html, test ok 

    
    def test_invalid_url(self):
        """ Returns for "/invalid" url, error 404"""
        response = self.client.post('/invalid/', data={'text': ''})
        self.assertEqual(response.status_code, 404)
        #if /invalid/ url returns 404, test is ok


    def test_code_of_user_login_in_template(self):
        """ Generate code for request.user login in template"""
        Link.objects.create(code="WcegF", usuario=self.user)
        self.client.login(username='wane', password='wane')
        response = self.client.get('/')
        self.assertContains(response, 'WcegF')
        #login user and code of data base in template 


    def test_generated_url_assigned_to_the_user(self):
        """ Imput url in template registered in data base"""
        self.client.login(username='wane', password='wane')
        response = self.client.post('/', data={'url': 'http://www.google.com'})
        genereated_url = Link.objects.get(url="http://www.google.com")
        self.assertContains(response, genereated_url.url)
        self.assertEqual(self.user, genereated_url.usuario)
        #login user and input url registered in database


    def test_url_not_passed(self):
        """ If post input url is None """
        response = self.client.post('/')
        self.assertContains(response, "Invalid URL")
        #imput form url field not post, return string "Invalid URL"


    def test_wrong_url(self):
        """ If post input url is not None and not valid"""
        response = self.client.post('/', data={'url': 'tomate'})
        self.assertContains(response, "Invalid URL")
        #client post bad url form returns "Invalid URL"


    def test_saved_if_not_logged(self):
        """ User not registered input saved url in data base"""
        response = self.client.post('/', data={'url':'http://www.google.com'})
        links = Link.objects.all()
        self.assertEqual(1, len(links))
        genereated_code = Link.objects.get(url="http://www.google.com")
        self.assertIsNone(genereated_code.usuario)
        #client post url in home.html saved and reguistered in the same object in model.
        