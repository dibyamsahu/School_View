from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basicapp.models import School, Students
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListView(ListView):
    context_object_name = "schools"
    model = School

class SchoolDetailView(DetailView):
    context_object_name = "school_details"
    model = School
    template_name = "basicapp/school_details.html"

class CreateSchool(CreateView):
    model = School
    fields = ("name", "principal", "location")
    template_name = "basicapp/school_form.html"

class UpdateSchool(UpdateView):
    model =School
    fields = ("name", "principal")

class DeleteSchool(DeleteView):
    model = School
    success_url = reverse_lazy("basicapp:list")