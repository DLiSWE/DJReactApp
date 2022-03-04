from django.views.generic import TemplateView, ListView

class HomePage(TemplateView):
    template_name = 'index.html'
