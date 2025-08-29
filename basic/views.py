from django.shortcuts import render
from django.views.generic import TemplateView

# pagina de inicio
class HomeView(TemplateView):
    template_name = 'home.html'

# página del chat
class ChatView(TemplateView):
    template_name = 'chat.html'

class RegistroView(TemplateView):
    template_name = 'registro.html'

class HistoryView(TemplateView):
    template_name = 'history.html'

from django.views.generic import ListView
from .models import Registro

class HistoryView(ListView):
    model = Registro  # el modelo
    template_name = 'history.html'  # el template
    context_object_name = 'registros'  # el contexto
    ordering = ['-created_at']  # el orden

