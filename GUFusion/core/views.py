"""Core Views"""
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm
from .models import Service, Team


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects\
            .order_by('?')\
            .all()
        context['team'] = Team.objects\
            .order_by('?')\
            .all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail sent successfully')
        return super(IndexView, self).form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Something went wrong')
        return super(IndexView, self).form_invalid(form)
