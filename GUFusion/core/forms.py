"""Core Form"""
from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name',
                           max_length=100)
    email = forms.CharField(label='E-mail',
                            max_length=100)
    subject = forms.CharField(label='Subject',
                              max_length=100)
    message = forms.CharField(label='Message',
                              widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        body = f'Name: {name} ' \
               f'Email: {email} ' \
               f'Subject: {subject} ' \
               f'Message: {message} '
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email='no-reply@fusion.com',
            to='no-reply@fusion.com',
            headers={'Reply-to': email}
        )
        mail.send()
