"""
Context processors for MedicoCave website.

Makes certain variables available to all templates.
"""
from django.conf import settings


def whatsapp_phone(request):
    """
    Makes WhatsApp phone number available to all templates.
    """
    return {
        'whatsapp_phone': settings.WHATSAPP_PHONE_NUMBER,
    }

