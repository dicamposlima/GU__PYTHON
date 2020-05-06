"""Core Form"""
from django.core.mail.message import EmailMessage
from django import forms
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',
                           max_length=100)
    email = forms.EmailField(label='Email',
                             max_length=100)
    assunto = forms.CharField(label='Assunto',
                              max_length=120)
    mensagem = forms.CharField(label='Mensagem',
                               widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome: {nome}' \
                   f' Email: {email}' \
                   f' Assunto: {assunto}' \
                   f' Mensagem: {mensagem}'
        mail = EmailMessage(
            subject=f'E-mail enviado - {assunto}',
            body=conteudo,
            from_email='no-reply@diego.com.br',
            to=['no-reply@diego.com.br'],
            headers={'Reply-to': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
