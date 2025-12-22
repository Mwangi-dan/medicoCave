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


def contact_info(request):
    """
    Makes contact information available to all templates.
    """
    return {
        'contact_email': settings.CONTACT_EMAIL,
        'contact_phone': settings.CONTACT_PHONE,
        'contact_instagram': settings.CONTACT_INSTAGRAM,
        'contact_facebook': settings.CONTACT_FACEBOOK,
        'contact_twitter': settings.CONTACT_TWITTER,
        'whatsapp_phone': settings.WHATSAPP_PHONE_NUMBER,
    }

