# MedicoCave Marketing Website

A high-performing, SEO-optimized, mobile-first marketing website for the MedicoCave mobile application. Built with Django, Tailwind CSS, and modern web best practices.

## Features

- ✅ **SEO-Optimized**: Meta tags, schema markup, semantic HTML
- ✅ **Mobile-First Design**: Fully responsive across all devices
- ✅ **Dark/Light Mode**: Toggle with localStorage persistence
- ✅ **Accessibility (A11y)**: WCAG compliant with proper ARIA attributes
- ✅ **Modern UI**: Clean design with accent color #01BFA8
- ✅ **Single-Page Landing**: Smooth scrolling navigation

## Technology Stack

- **Backend**: Django 4.2+
- **Frontend**: HTML5, Tailwind CSS (CDN), Vanilla JavaScript
- **Database**: SQLite (minimal, for future expansion if needed)

## Setup Instructions

### 1. Install Dependencies

```bash
# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Django
pip install -r requirements.txt
```

### 2. Run Migrations (Optional - for future database features)

```bash
python manage.py migrate
```

### 3. Run the Development Server

```bash
python manage.py runserver
```

The website will be available at `http://127.0.0.1:8000/`

## Project Structure

```
medicocave/
├── manage.py
├── requirements.txt
├── medicocave/          # Django project settings
│   ├── __init__.py
│   ├── settings.py      # Minimal Django configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py
└── website/             # Main app
    ├── __init__.py
    ├── apps.py
    ├── views.py         # Index view
    └── templates/
        └── website/
            ├── base.html    # Base template with SEO & dark mode
            └── index.html   # Main landing page
```

## Key Design Elements

- **Accent Color**: `#01BFA8` (rgb(1, 191, 168)) - Used for CTAs, headings, and key accents
- **Color Modes**: Light (default) and Dark mode with smooth transitions
- **Mobile-First**: All components designed for mobile, enhanced for desktop
- **Touch-Friendly**: Minimum 44x44px touch targets for mobile

## SEO Features

- Dynamic meta tags (title, description, keywords)
- Open Graph and Twitter Card meta tags
- Schema.org structured data (MobileApplication)
- Semantic HTML5 elements
- Descriptive alt text for images
- Clean, crawlable URLs

## Sections

1. **Navigation Bar**: Fixed/sticky with logo, nav links, CTA button, and theme toggle
2. **Hero Section**: Compelling H1, value proposition, primary CTA
3. **Features**: 4 key benefits with icons
4. **How It Works**: 3-step process
5. **Why Choose Us**: Trust indicators and social proof
6. **FAQ**: Collapsible accordion with 4 questions
7. **Footer**: Company info, links, secondary CTA

## Customization

### Update App Store Links

Edit the download buttons in `index.html` (search for "Download for iOS" and "Download for Android") and replace the `href="#"` with your actual app store URLs.

### Update Images

Replace the placeholder app mockup in the hero section with actual screenshots of your mobile app.

### Modify Content

All content is in `website/templates/website/index.html`. Update text, features, and FAQ items as needed.

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Update `SECRET_KEY` with a secure random key
3. Configure `ALLOWED_HOSTS` with your domain
4. Set up proper static file serving (e.g., WhiteNoise or CDN)
5. Use a production database (PostgreSQL recommended)
6. Enable HTTPS
7. Set up proper error logging

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## License

Copyright © 2024 MedicoCave. All rights reserved.

