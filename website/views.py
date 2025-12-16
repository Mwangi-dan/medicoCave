"""
Views for MedicoCave website.

Simple view for the marketing landing page.
"""
from django.shortcuts import render


def index(request):
    """
    Homepage view - Single-page marketing site.
    
    SEO-optimized landing page for MedicoCave mobile app.
    """
    context = {
        'page_title': 'MedicoCave: Connect with Top Doctors. Your Health, Simplified.',
        'meta_description': 'MedicoCave connects patients with trusted medical professionals. Find specialists, book consultations, and manage your health records securely. Download the app today.',
        'meta_keywords': 'medical app, doctor consultation, healthcare, patient portal, medical professionals, health app',
    }
    return render(request, 'website/index.html', context)

