from django.urls import path, include
from .views import HomeView, ChatView, RegistroView, HistoryView, ApiProjectsView
from . import views
from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()
router.register('api.projects', ProjectViewSet, 'projects')
urlpatterns = router.urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('chat/', ChatView.as_view(), name='chat'),
    path('registro/', RegistroView.as_view(), name='registro'),
    #path('api/api.projects/', views.api_projects, name='api_projects'),
    path('api/', include(router.urls)),  # aca se incluyen las URLs de la API
    path('history/', HistoryView.as_view(), name='history'), 
    path('api/projects/', ApiProjectsView.as_view(), name='api-projects'),
]


