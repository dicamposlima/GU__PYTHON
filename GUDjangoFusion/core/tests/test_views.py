"""Core View Test"""
from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
    def setUp(self) -> None:
        self.payload = {
            'name': 'Diego',
            'email': 'di@gmail.com',
            'subject': 'Algum assunto',
            'message': 'Alguma mensagem',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'),
                                   data=self.payload)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        self.payload = {
            'name': 'Diego',
            'subject': 'Algum assunto',
        }
        request = self.client.post(reverse_lazy('index'),
                                   data=self.payload)
        self.assertEquals(request.status_code, 200)
