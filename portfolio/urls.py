from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import HomeView, ProjectsView, ExperienceView, ContactView
router = DefaultRouter()
router.register(r'home', HomeView, basename='home')
router.register(r'projects', ProjectsView, basename='projects')
router.register(r'experience',ExperienceView, basename='experience')
router.register(r'contact', ContactView, basename='contact')

urlpatterns = [  ]

urlpatterns += router.urls
