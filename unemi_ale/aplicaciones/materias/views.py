from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import * 
# Create your views here.
class IndexMaterias(TemplateView):
    template_name = "indexMateria.html"
    
class AddDateFormMateria(CreateView):
    template_name = "formMateria.html"
    model = Cursos
    fields = "__all__"
    success_url = "/indexMateria"
    
class ListAllMateria(ListView):
    template_name= "indexMateria.html"
    model = Cursos
    context_object_name = "course"
    
class UpdateMaterias(UpdateView):
    template_name= "updateMateria.html"
    model= Cursos
    fields= "__all__"
    success_url = "/indexMateria"
    