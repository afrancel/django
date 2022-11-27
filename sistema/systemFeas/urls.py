from django.urls import URLPattern, path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('bicis', views.bicis, name='bicis'),
    path('bicis/crear', views.crear, name='crear'),
    path('bicis/editar', views.editar, name='editar'),
    path('bicis/editar/<int:id>',views.editar, name='editar'),
    path('eliminar/<int:id>',views.eliminar, name='eliminar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)