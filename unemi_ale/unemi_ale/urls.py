"""
URL configuration for unemi_ale project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from aplicaciones.docente.views import *
from aplicaciones.materias.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', ListAll.as_view()),
    path('addDateFormDocent/', AddDateFormDocent.as_view()),
    path('formMateria', AddDateFormMateria.as_view()),
    path('indexMateria',  ListAllMateria.as_view()),
    path('updateDocente/<pk>/',  UpdateDocente.as_view()),
    path('updateMateria/<pk>/',  UpdateMaterias.as_view()),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
