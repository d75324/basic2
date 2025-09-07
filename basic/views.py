from django.shortcuts import render
from django.views.generic import TemplateView

# requerido para procesar los POST de la SPA
from django.utils.decorators import method_decorator
#from django.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

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


# vista para procesar los POST de la SPA
@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(require_http_methods(["POST", "OPTIONS"]), name='dispatch')
class ApiProjectsView(APIView):
    # Maneja las solicitudes OPTIONS para CORS
    def options(self, request, *args, **kwargs):
        response = Response({"status": "ok"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # Maneja las solicitudes POST
    def post(self, request, *args, **kwargs):
        try:
            # En DRF usamos request.data para ver la data que está llegando
            data = request.data

            # Debug: ver qué está llegando
            print("Datos recibidos:", data)
            print("=== DEBUG URL ===")
            print("URL completa:", request.build_absolute_uri())
            print("Path:", request.path)
            print("Método:", request.method)
            print("=== FIN DEBUG URL ===")

            print("=== DEBUG HEADERS ===")
            for header, value in request.headers.items():
                print(f"{header}: {value}")
            print("=== FIN DEBUG HEADERS ===")

            # Validar campos requeridos
            required_fields = ['name', 'email', 'color', 'fruit', 'message']
            for field in required_fields:
                if field not in data:
                    error_response = Response({
                        'error': f'Campo faltante: {field}'
                    }, status=status.HTTP_400_BAD_REQUEST)
                    # Headers de CORS para manejar errores
                    error_response["Access-Control-Allow-Origin"] = "*"
                    return error_response

            # Crear nuevo registro
            registro = Registro.objects.create(
                name=data['name'],
                email=data['email'],
                color=data['color'],
                fruit=data['fruit'],
                message=data['message']
            )

            # Respuesta de éxito CON HEADERS CORS
            response = Response({
                'status': 'success',
                'message': 'Registro creado correctamente',
                'id': registro.id,
                'data': {
                    'name': registro.name,
                    'email': registro.email,
                    'color': registro.color,
                    'fruit': registro.fruit,
                    'message': registro.message
                }
            }, status=status.HTTP_201_CREATED)
            
            # headers CORS criticos para POST
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            
            return response

        except Exception as e:
            error_response = Response({'error': str(e)},
                          status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            # headers CORS para errores
            error_response["Access-Control-Allow-Origin"] = "*"
            return error_response 
