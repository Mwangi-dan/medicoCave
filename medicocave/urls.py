"""
URL configuration for MedicoCave project.

SEO-friendly URL structure for the marketing website.
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from website import views

urlpatterns = [
    # Homepage - SEO-optimized clean URL
    path('', views.index, name='index'),
]

