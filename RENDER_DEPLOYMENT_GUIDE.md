# Braymell Django App - Render Deployment Guide

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [Step-by-Step Deployment](#step-by-step-deployment)
- [Environment Variables Setup](#environment-variables-setup)
- [Post-Deployment Verification](#post-deployment-verification)
- [Troubleshooting](#troubleshooting)
- [Database Management](#database-management)
- [Static Files & Media](#static-files--media)

---

## Prerequisites

Before deploying to Render, ensure you have:

1. **GitHub Account** - Push your code to GitHub
2. **Render Account** - Sign up at [render.com](https://render.com)
3. **PostgreSQL Database** - Create a PostgreSQL instance (can be on Render or external provider like Supabase)
4. **Cloudinary Account** - For media storage (already configured in settings)
5. **Git** - For version control

---

## Pre-Deployment Checklist

- [ ] All code committed to GitHub
- [ ] `requirements.txt` is up to date: `pip freeze > requirements.txt`
- [ ] `runtime.txt` specifies Python version: `python-3.11.9`
- [ ] `Procfile` exists at root level
- [ ] `build.sh` and `start.sh` scripts are executable
- [ ] Database migrations are ready
- [ ] All sensitive data is in environment variables (NOT hardcoded)
- [ ] `DEBUG = False` in production settings
- [ ] `ALLOWED_HOSTS` includes your Render domain
- [ ] Static files configuration is correct
- [ ] CORS settings are properly configured

---

## Step-by-Step Deployment

### 1. Push Code to GitHub

```bash
# Navigate to your project directory
cd /home/peterson/Desktop/braymell/BRAYMELLS\ \(Copy\ 1\)/backend

# Initialize git (if not already done)
git init
git add .
git commit -m "Prepare for Render deployment"

# Add remote and push (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/braymell.git
git push -u origin main
```

### 2. Create Render Web Service

1. Log in to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Web Service"**
3. Select your GitHub repository (braymell)
4. Configure as follows:

   | Field             | Value                              |
   | ----------------- | ---------------------------------- |
   | **Name**          | braymell (or your preferred name)  |
   | **Environment**   | Python 3                           |
   | **Build Command** | `bash build.sh`                    |
   | **Start Command** | `gunicorn config.wsgi:application` |
   | **Plan**          | Starter (or higher)                |

### 3. Create PostgreSQL Database on Render

1. Click **"New +"** → **"PostgreSQL"**
2. Configure as follows:

   | Field        | Value               |
   | ------------ | ------------------- |
   | **Name**     | braymell-db         |
   | **Database** | braymell            |
   | **User**     | braymell_user       |
   | **Region**   | Same as web service |
   | **Plan**     | Free (or Starter)   |

3. Copy the **Internal Database URL** (you'll need this for the web service)

### 4. Configure Environment Variables

Go to your Web Service settings → **"Environment"** and add these variables:

#### Essential Variables:

```
SECRET_KEY=your-secret-key-here
DEBUG=False

# Database (from PostgreSQL service)
DATABASE_URL=postgresql://braymell_user:password@dpg-xxxxx.onrender.com:5432/braymell

# Cloudinary (for media storage)
CLOUDINARY_CLOUD_NAME=your-cloudinary-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret

# CORS
CORS_ALLOWED_ORIGINS=https://braymell.onrender.com,https://www.braymell.com

# Django
ALLOWED_HOSTS=braymell.onrender.com,www.braymell.com,localhost,127.0.0.1
```

### 5. Generate Secret Key (if needed)

If you need a new SECRET_KEY, generate one:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

---

## Environment Variables Setup

### Critical Variables Explained:

#### `SECRET_KEY`

- Used for cryptographic signing
- Generate a strong random key
- Keep it secret - never commit to git

#### `DATABASE_URL`

- Format: `postgresql://username:password@host:port/database`
- Render provides this when you create a PostgreSQL service
- Can also use external PostgreSQL (Supabase, AWS RDS, etc.)

#### `CLOUDINARY_*`

- Get from your Cloudinary dashboard
- Used for image uploads and storage
- Already configured in `settings.py`

#### `ALLOWED_HOSTS`

- Add all domains that will access your site
- Include Render domain: `braymell.onrender.com`
- Include custom domains if applicable

#### `CSRF_TRUSTED_ORIGINS`

- Add all domains for CSRF protection
- Format: `https://yourdomain.com`

---

## Settings.py Update for Render

The project already has most settings configured, but verify:

```python
# settings.py should have:

# Read from environment
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = False  # Always False in production

# Database from environment
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}

# Static files with WhiteNoise
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Allowed hosts
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# CORS
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')
```

### ⚠️ Important Settings Update Needed

Update `config/settings.py` to read `ALLOWED_HOSTS` and `CORS_ALLOWED_ORIGINS` from environment variables:

```python
# Change from hardcoded values to:
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

CORS_ALLOWED_ORIGINS = os.environ.get(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:3000'
).split(',')
```

---

## Post-Deployment Verification

### 1. Check Render Deployment Status

1. Go to Render Dashboard → Your Web Service
2. Check the **"Logs"** tab for errors
3. Look for successful deployment message

### 2. Test the Application

```bash
# Test homepage
curl https://braymell.onrender.com/

# Test API
curl https://braymell.onrender.com/api/v1/projects/

# Test admin
https://braymell.onrender.com/admin/
```

### 3. Run Migrations on Render

If migrations didn't run automatically:

1. Go to Web Service → **"Shell"** (top right)
2. Run: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`

### 4. Check Static Files

- Static files should be served correctly at `/static/`
- Images should load from Cloudinary

### 5. Monitor Logs

Keep checking logs for any runtime errors:

```
Render Dashboard → Your Web Service → Logs
```

---

## Database Management

### Initial Setup

1. **On Render Shell**, run:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

2. **Load initial data** (if you have fixtures):
   ```bash
   python manage.py loaddata initial_data.json
   ```

### Backup PostgreSQL

1. From Render Dashboard → PostgreSQL Database
2. Click **"Backups"** tab
3. Create manual backup before major changes

### Connect to Remote Database Locally

```bash
# Install psql if needed
# Then use the DATABASE_URL from Render

psql postgresql://username:password@host:5432/database_name
```

---

## Static Files & Media

### Static Files (CSS, JS, Images)

- Handled by **WhiteNoise** middleware
- Automatically collected on deployment (`build.sh` runs `collectstatic`)
- Served from `/staticfiles/` directory

### Media Files (User Uploads)

- Configured to use **Cloudinary** storage
- `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`
- Images upload directly to Cloudinary
- No local storage needed on Render

### Testing Static Files

```bash
# After deployment, verify CSS loads:
curl -I https://braymell.onrender.com/static/css/style.css

# Should return 200 OK
```

---

## Troubleshooting

### Common Issues

#### 1. **502 Bad Gateway Error**

**Causes:**

- App crashed during startup
- Database connection failed
- Missing environment variables

**Solution:**

```bash
# Check logs in Render Dashboard
# Look for specific error messages
# Verify all environment variables are set
# Check DATABASE_URL format
```

#### 2. **Static Files Not Loading**

**Causes:**

- `collectstatic` command failed
- WhiteNoise not configured

**Solution:**

```bash
# In Render Shell:
python manage.py collectstatic --no-input --clear

# Check STORAGES configuration in settings.py
```

#### 3. **Database Connection Error**

**Causes:**

- Invalid DATABASE_URL
- Database not running
- Wrong credentials

**Solution:**

```bash
# Test connection in Render Shell:
python manage.py dbshell

# Verify DATABASE_URL format
# Check PostgreSQL service is running
```

#### 4. **Import/Module Errors**

**Causes:**

- Missing package in `requirements.txt`
- Wrong Python version

**Solution:**

```bash
# Update requirements.txt locally:
pip freeze > requirements.txt

# Commit and push
git add requirements.txt
git commit -m "Update dependencies"
git push

# Redeploy from Render Dashboard
```

#### 5. **Cloudinary Images Not Showing**

**Causes:**

- Missing Cloudinary credentials
- Incorrect API keys
- Files not actually uploaded

**Solution:**

- Verify credentials in Render Environment Variables
- Check Cloudinary dashboard for uploads
- Re-upload files if needed

#### 6. **CORS Issues**

**Cause:**

- Frontend domain not in `CORS_ALLOWED_ORIGINS`

**Solution:**

```bash
# Update environment variable:
CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://braymell.onrender.com

# Redeploy
```

---

## Manual Deployment Steps (if needed)

### Redeploy Application

1. Go to Web Service → **"Deploy"** button (top right)
2. Select branch (usually `main`)
3. Click **"Deploy"**

### View Real-time Logs

1. Web Service → **"Logs"** tab
2. Refresh for latest entries

### Access App Shell

1. Web Service → Click **"Shell"** (top right corner)
2. Run Django management commands:
   ```bash
   python manage.py createsuperuser
   python manage.py migrate
   python manage.py shell
   ```

---

## Performance & Monitoring

### Enable Render Metrics

1. Go to Web Service settings
2. Enable **"Metrics"** to monitor:
   - CPU usage
   - Memory usage
   - Request count
   - Response times

### Optimize Performance

1. **Database Queries**: Use `select_related()` and `prefetch_related()`
2. **Caching**: Consider adding Redis
3. **CDN**: Use Cloudinary for image optimization
4. **Pagination**: Already configured (9 items per page)

---

## Custom Domain Setup

1. In Render Dashboard → Web Service → **"Settings"**
2. Scroll to **"Custom Domains"**
3. Add your domain (e.g., `braymell.com`)
4. Follow DNS configuration instructions
5. Update environment variables:
   ```
   ALLOWED_HOSTS=braymell.com,www.braymell.com,braymell.onrender.com
   CSRF_TRUSTED_ORIGINS=https://braymell.com,https://www.braymell.com
   ```

---

## Security Checklist

- [ ] `SECRET_KEY` is strong and unique
- [ ] `DEBUG = False` in production
- [ ] Database credentials never in source code
- [ ] HTTPS enforced (Render does this automatically)
- [ ] CORS properly configured
- [ ] CSRF protection enabled
- [ ] Admin interface password is strong
- [ ] Regular backups scheduled
- [ ] Monitor logs for suspicious activity

---

## Useful Commands

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Collect static files
python manage.py collectstatic
```

### Render Shell Commands

```bash
# View database tables
python manage.py dbshell

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Execute Python code
python manage.py shell

# Clear cache
python manage.py clear_cache
```

---

## Support & Resources

- **Render Docs**: https://render.com/docs
- **Django Docs**: https://docs.djangoproject.com/
- **WhiteNoise Docs**: http://whitenoise.evans.io/
- **Cloudinary Docs**: https://cloudinary.com/documentation
- **PostgreSQL**: https://www.postgresql.org/docs/

---

## Quick Reference: File Locations

```
backend/
├── Procfile                    # Process types for Render
├── build.sh                    # Build script (executed by Render)
├── start.sh                    # Local start script
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version (3.11.9)
├── manage.py                   # Django management
├── config/
│   ├── settings.py            # Django settings
│   ├── wsgi.py                # WSGI application
│   └── urls.py                # URL configuration
├── core/
│   ├── views.py               # View logic
│   ├── models.py              # Database models
│   ├── urls.py                # App URLs
│   ├── templates/             # HTML templates
│   ├── static/                # Static files
│   └── migrations/            # Database migrations
└── staticfiles/               # Collected static files (generated)
```

---

## Final Checklist Before Going Live

- [ ] All code pushed to GitHub
- [ ] All environment variables set in Render
- [ ] Database migrations completed
- [ ] Superuser created
- [ ] Static files collected
- [ ] Admin panel works
- [ ] Public pages display correctly
- [ ] Images load from Cloudinary
- [ ] No console errors in logs
- [ ] CORS configured correctly
- [ ] Database backed up
- [ ] Monitoring enabled
- [ ] Domain configured (if custom)

---

**Deployment completed! Your Braymell app should now be live on Render. 🚀**

For questions or issues, check the Logs tab in your Render Dashboard first, then refer to the Troubleshooting section above.
