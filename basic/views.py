from django.shortcuts import render
from django.views.generic import TemplateView

# requerido para procesar los POST de la SPA
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import Registro

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
@csrf_exempt  
@require_http_methods(["POST", "OPTIONS"])  # Acepta POST y OPTIONS
def api_projects(request):
    # preflight OPTIONS para CORS
    if request.method == "OPTIONS":
        response = JsonResponse({"status": "ok"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
    
    # POST request
    if request.method == "POST":
        try:
            # Decodificar JSON
            data = json.loads(request.body)
            
            # Debug: ver qué está llegando
            print("Datos recibidos:", data)
            
            # Validar campos requeridos
            required_fields = ['name', 'email', 'color', 'fruit', 'message']
            for field in required_fields:
                if field not in data:
                    return JsonResponse({
                        'error': f'Campo faltante: {field}'
                    }, status=400)
            
            # Crear nuevo registro
            registro = Registro.objects.create(
                name=data['name'],
                email=data['email'],
                color=data['color'],
                fruit=data['fruit'],
                message=data['message']
            )
            
            # Respuesta de éxito
            return JsonResponse({
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
            }, status=201)
            
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


