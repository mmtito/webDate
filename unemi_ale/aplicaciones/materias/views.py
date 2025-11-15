from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import * 
# Create your views here.

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
    
class DeleteMaterias(DeleteView):
    template_name = "deleteMateria.html"
    model = Cursos
    success_url = "/indexMateria"
    context_object_name = "delete"