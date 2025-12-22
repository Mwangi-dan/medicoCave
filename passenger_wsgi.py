"""
Passenger WSGI entry point for MedicoCave project.

This file is used by Phusion Passenger (commonly used on shared hosting)
to serve the Django application. Passenger will automatically detect this
file and use it to run your Django application.

For more information, see:
https://www.phusionpassenger.com/library/walkthroughs/deploy/python/ownserver/nginx/oss/install_wrapper.html
"""

import os
import sys

# Add the project directory to the Python path
# Adjust this path if your project is located elsewhere
sys.path.insert(0, os.path.dirname(__file__))

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicocave.settings')

# Import the WSGI application
from django.core.wsgi import get_wsgi_application

# Create the WSGI application object
application = get_wsgi_application()

