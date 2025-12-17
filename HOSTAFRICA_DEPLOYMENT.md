# Deploy MedicoCave to HostAfrica

This guide will help you deploy your MedicoCave website to HostAfrica and connect it to your domain **medicocave.co.ke**.

## Prerequisites

- ✅ Domain purchased: `medicocave.co.ke`
- ✅ Server/hosting account with HostAfrica
- ✅ SSH access to your server
- ✅ Python 3.8+ installed on server
- ✅ Git installed on server

## Step 1: Server Setup

### 1.1 Connect to Your Server

SSH into your HostAfrica server:
```bash
ssh username@your-server-ip
```

### 1.2 Install Required Software

```bash
# Update system packages
sudo apt update
sudo apt upgrade -y

# Install Python and pip (if not already installed)
sudo apt install python3 python3-pip python3-venv -y

# Install Nginx (web server)
sudo apt install nginx -y

# Install Git (if not already installed)
sudo apt install git -y
```

### 1.3 Create Application Directory

```bash
# Create directory for your application
sudo mkdir -p /var/www/medicocave
sudo chown $USER:$USER /var/www/medicocave
cd /var/www/medicocave
```

## Step 2: Deploy Your Code

### 2.1 Clone Your Repository

```bash
cd /var/www/medicocave
git clone https://github.com/Mwangi-dan/medicoCave.git .
```

### 2.2 Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2.3 Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 2.4 Configure Environment Variables

Create a `.env` file in the project root:
```bash
nano .env
```

Add the following (replace with your actual values):
```env
SECRET_KEY=your-very-secure-secret-key-here-generate-a-new-one
DEBUG=False
ALLOWED_HOSTS=medicocave.co.ke,www.medicocave.co.ke
WHATSAPP_PHONE_NUMBER=254725899912
```

**Generate a secure SECRET_KEY:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 2.5 Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## Step 3: Configure Gunicorn

### 3.1 Test Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 medicocave.wsgi:application
```

Visit `http://your-server-ip:8000` to test. Press `Ctrl+C` to stop.

### 3.2 Create Gunicorn Service

Create a systemd service file:
```bash
sudo nano /etc/systemd/system/medicocave.service
```

Add the following content:
```ini
[Unit]
Description=MedicoCave Gunicorn daemon
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/medicocave
Environment="PATH=/var/www/medicocave/venv/bin"
ExecStart=/var/www/medicocave/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/medicocave/medicocave.sock \
    medicocave.wsgi:application

[Install]
WantedBy=multi-user.target
```

**Note:** Replace `www-data` with your username if you're not using the default web user.

### 3.3 Start and Enable the Service

```bash
sudo systemctl daemon-reload
sudo systemctl start medicocave
sudo systemctl enable medicocave
sudo systemctl status medicocave
```

## Step 4: Configure Nginx

### 4.1 Create Nginx Configuration

```bash
sudo nano /etc/nginx/sites-available/medicocave
```

Add the following configuration:
```nginx
server {
    listen 80;
    server_name medicocave.co.ke www.medicocave.co.ke;

    # Redirect www to non-www (optional, adjust as needed)
    # if ($host = www.medicocave.co.ke) {
    #     return 301 http://medicocave.co.ke$request_uri;
    # }

    location /static/ {
        alias /var/www/medicocave/staticfiles/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/medicocave/medicocave.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 4.2 Enable the Site

```bash
sudo ln -s /etc/nginx/sites-available/medicocave /etc/nginx/sites-enabled/
sudo nginx -t  # Test configuration
sudo systemctl restart nginx
```

## Step 5: Configure DNS at HostAfrica

### 5.1 Access DNS Management

1. Log into your HostAfrica control panel
2. Navigate to **Domain Management** → **DNS Management**
3. Select your domain: `medicocave.co.ke`

### 5.2 Configure DNS Records

Add or update the following DNS records:

**A Record (IPv4):**
- **Type:** A
- **Name:** @ (or leave blank for root domain)
- **Value:** Your server's IP address
- **TTL:** 3600 (or default)

**A Record for www:**
- **Type:** A
- **Name:** www
- **Value:** Your server's IP address
- **TTL:** 3600 (or default)

**Optional - CNAME (if you prefer):**
- **Type:** CNAME
- **Name:** www
- **Value:** medicocave.co.ke
- **TTL:** 3600

### 5.3 DNS Propagation

DNS changes can take 24-48 hours to propagate, but usually happen within a few hours. You can check propagation status at:
- https://www.whatsmydns.net/#A/medicocave.co.ke

## Step 6: SSL Certificate (HTTPS)

### 6.1 Install Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 6.2 Obtain SSL Certificate

```bash
sudo certbot --nginx -d medicocave.co.ke -d www.medicocave.co.ke
```

Follow the prompts:
- Enter your email address
- Agree to terms of service
- Choose whether to redirect HTTP to HTTPS (recommended: Yes)

### 6.3 Auto-Renewal

Certbot automatically sets up renewal. Test it:
```bash
sudo certbot renew --dry-run
```

## Step 7: Firewall Configuration

If you have a firewall enabled, allow HTTP and HTTPS:

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
```

## Step 8: Final Verification

1. **Check Gunicorn service:**
   ```bash
   sudo systemctl status medicocave
   ```

2. **Check Nginx service:**
   ```bash
   sudo systemctl status nginx
   ```

3. **Test your website:**
   - Visit: `http://medicocave.co.ke`
   - Visit: `https://medicocave.co.ke` (after SSL setup)

## Updating Your Site

When you make changes and push to GitHub:

```bash
cd /var/www/medicocave
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
sudo systemctl restart medicocave
```

## Troubleshooting

### Check Logs

**Gunicorn logs:**
```bash
sudo journalctl -u medicocave -f
```

**Nginx logs:**
```bash
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/nginx/access.log
```

### Common Issues

1. **502 Bad Gateway:**
   - Check Gunicorn is running: `sudo systemctl status medicocave`
   - Check socket permissions: `ls -la /var/www/medicocave/medicocave.sock`
   - Ensure Nginx user has access to the socket

2. **Static files not loading:**
   - Run: `python manage.py collectstatic --noinput`
   - Check Nginx static file path matches `STATIC_ROOT` in settings.py

3. **Domain not resolving:**
   - Verify DNS records are correct
   - Wait for DNS propagation (can take up to 48 hours)
   - Check DNS with: `dig medicocave.co.ke` or `nslookup medicocave.co.ke`

4. **Permission errors:**
   - Ensure proper ownership: `sudo chown -R www-data:www-data /var/www/medicocave`
   - Check file permissions: `chmod -R 755 /var/www/medicocave`

## Security Checklist

- ✅ `DEBUG=False` in production
- ✅ Strong `SECRET_KEY` in `.env` file
- ✅ `.env` file not in version control (check `.gitignore`)
- ✅ SSL certificate installed (HTTPS)
- ✅ Firewall configured
- ✅ Regular system updates: `sudo apt update && sudo apt upgrade`

## Support

If you encounter issues:
1. Check the logs (see Troubleshooting section)
2. Verify all steps were completed correctly
3. Contact HostAfrica support for server/DNS issues
4. Check Django documentation: https://docs.djangoproject.com/

---

**Your site should now be live at https://medicocave.co.ke! 🚀**

