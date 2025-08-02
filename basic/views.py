from django.shortcuts import render
from django.views.generic import TemplateView

# pagina de inicio
class HomeView(TemplateView):
    template_name = 'home.html'

# página del chat
class ChatView(TemplateView):
    template_name = 'chat.html'