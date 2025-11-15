from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView,  UpdateView
from .models import * 

# Create your views here.

class IndexDocente(TemplateView):
    template_name= "inicio.html"
    
class AddDateFormDocent (CreateView):
    template_name= "formDocente.html"
    model = Docente
    fields = "__all__"
    success_url = "/inicio"

class ListAll(ListView):
    template_name = "inicio.html"
    model = Docente
    context_object_name = "teacher"

class UpdateDocente (UpdateView):
    template_name = "updateDocente.html"
    model = Docente
    fields = "__all__"
    success_url = "/inicio"
    
class DeleteDocente (DeleteView):
    template_name = "deleteDocente.html"
    model = Docente
    success_url = "/inicio"
    context_object_name = "delete"