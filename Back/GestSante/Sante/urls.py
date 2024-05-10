from django.urls import  path
from GestSante import settings
from django.conf.urls.static import static
from Sante import views

urlpatterns = [
    
    path('mettre-en-operation/<int:service_id>/', views.mettre_en_operation, name='mettre_en_operation'),
    path('mettre-hors-operation/<int:service_id>/', views.mettre_hors_operation, name='mettre_hors_operation'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)