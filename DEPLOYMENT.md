# Deploy MedicoCave to Render (Free)

This guide will help you deploy your MedicoCave website to Render's free tier in just a few minutes.

## Quick Steps

### 1. Create a Render Account
- Go to [render.com](https://render.com)
- Sign up for free (no credit card required for free tier)
- Connect your GitHub account

### 2. Deploy from GitHub
1. In Render dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository (`Mwangi-dan/medicoCave`)
3. Render will auto-detect the `render.yaml` file
4. Or manually configure:
   - **Name**: `medicocave` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn medicocave.wsgi:application`
   - **Plan**: Select **Free**

### 3. Environment Variables
Render will automatically:
- Generate a `SECRET_KEY` (configured in `render.yaml`)
- Set `DEBUG=False` for production

### 4. Deploy!
- Click **"Create Web Service"**
- Render will build and deploy your site
- Your site will be live at: `https://medicocave.onrender.com` (or your custom name)

## What Happens Next

1. **Build Phase**: Render installs dependencies and collects static files
2. **Deploy Phase**: Your site goes live
3. **Auto-Deploy**: Every push to `main` branch will automatically redeploy

## Free Tier Notes

- ✅ Free SSL certificate
- ✅ Custom domain support
- ⚠️ Service spins down after 15 minutes of inactivity (wakes up on first request)
- ⚠️ Build time: ~5-10 minutes

## Troubleshooting

If deployment fails:
1. Check the build logs in Render dashboard
2. Ensure all files are committed and pushed to GitHub
3. Verify `requirements.txt` includes all dependencies

## Alternative: Railway (Also Free)

If you prefer Railway:
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway auto-detects Django and deploys!

---

**Your site will be live in ~5-10 minutes!** 🚀

