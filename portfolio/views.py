from django.shortcuts import render
from django.views import View
from .models import Home, Projects, Experience, Contact, skill, SubSkill
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import HomeSerializer, ProjectsSerializer, ExperienceSerializer, ContactSerializer
# Create your views here.

class HomeView(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer

class ProjectsView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ExperienceView(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class ContactView(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

