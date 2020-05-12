"""Core Form Test"""
from django.test import TestCase

from core.forms import ContactForm


class ContactFormTestCase(TestCase):
    def setUp(self) -> None:
        self.name = 'Diego'
        self.email = 'di@gmail.com'
        self.subject = 'Algum assunto'
        self.message = 'Alguma mensagem'

        self.body = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
        }
        self.form = ContactForm(data=self.body)

    def test_send_mail(self):
        form1 = ContactForm(data=self.body)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
