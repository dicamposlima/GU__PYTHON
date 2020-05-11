"""Core Form"""
from django import forms
from django.core.mail.message import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(label=_('Nome'),
                           max_length=100)
    email = forms.CharField(label=_('E-mail'),
                            max_length=100)
    subject = forms.CharField(label=_('Assunto'),
                              max_length=100)
    message = forms.CharField(label=_('Mensagem'),
                              widget=forms.Textarea)

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        n = _('Nome')
        e = _('E-mail')
        a = _('Assunto')
        m = _('Mensagem')
        body = f'{n}: {name} ' \
               f'{e}: {email} ' \
               f'{a}: {subject} ' \
               f'{m}: {message} '
        mail = EmailMessage(
            subject=subject,
            body=body,
            from_email='no-reply@fusion.com',
            to=('no-reply@fusion.com',),
            headers={'Reply-to': email}
        )
        mail.send()
