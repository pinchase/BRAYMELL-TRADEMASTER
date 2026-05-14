# Render Deployment Troubleshooting Guide

Quick solutions for common issues when deploying to Render.

---

## 🔴 Critical Issues

### 1. 502 Bad Gateway Error

**What it means:** The web service crashed or failed to start

**Check logs:**

1. Go to Render Dashboard → Your Web Service
2. Click **"Logs"** tab
3. Look for error messages (usually red text)

**Common causes and fixes:**

#### A. Missing Environment Variables

```
Error: KeyError: 'SECRET_KEY' or similar
```

**Fix:**

- Go to "Environment" tab in Render
- Add missing variable
- Click "Deploy" to redeploy

#### B. Database Connection Failed

```
Error: psycopg2.OperationalError: FATAL: database does not exist
```

**Fix:**

1. Verify DATABASE_URL is correct:
   - Should be `postgresql://user:pass@host:port/db`
   - Check for typos in password
2. Verify PostgreSQL service is running
3. Check connection limits aren't exceeded

#### C. Port Already in Use

```
Error: Address already in use
```

**Fix:**

- Render automatically assigns ports
- No fix needed, restart the service
- Click "Restart" in Render Dashboard

#### D. Import/Module Not Found

```
Error: ModuleNotFoundError: No module named 'X'
```

**Fix:**

```bash
# Locally, update requirements
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push origin main
# Render will automatically redeploy
```

---

## 🟡 Common Issues

### 2. Static Files Not Loading (404 Errors)

**Symptoms:**

- CSS/JS files return 404
- Images don't load
- Styling is broken

**Logs show:**

```
"GET /static/css/style.css HTTP/1.1" 404
```

**Fix:**

```bash
# Option 1: Force recollection (in Render Shell)
python manage.py collectstatic --clear --noinput

# Option 2: Redeploy and let build script handle it
# (Click "Deploy" button in Render)

# Option 3: Check settings.py
# Verify STATIC_ROOT and STATIC_URL are correct
```

**Verify it worked:**

```bash
# SSH into Render shell and check
ls staticfiles/css/
# Should list your CSS files
```

### 3. Images Not Showing (Cloudinary)

**Symptoms:**

- Image placeholders appear as broken
- Cloudinary dashboard shows no uploads

**Causes:**

#### A. Missing Cloudinary Credentials

```
Error: CLOUDINARY_CLOUD_NAME is None
```

**Fix:**

1. Go to https://cloudinary.com/console
2. Copy your credentials
3. Add to Render Environment Variables:
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`

#### B. Wrong Credentials

**Fix:**

1. Double-check credentials in Cloudinary dashboard
2. Update in Render Environment Variables
3. Click "Deploy" to redeploy

#### C. Files Never Uploaded

**Fix:**

1. Upload images through admin panel again
2. Or upload directly to Cloudinary

### 4. Migrations Not Running

**Symptoms:**

- Database tables don't exist
- 500 error about missing tables

**Logs show:**

```
ProgrammingError: relation "core_client" does not exist
```

**Fix:**

#### Option 1: Via Render Shell (Recommended)

1. Go to Web Service → Click **"Shell"** (top right)
2. Run:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

#### Option 2: Via Procfile

Ensure Procfile includes:

```
release: python manage.py migrate
web: gunicorn config.wsgi:application
```

Then redeploy:

- Click "Deploy" button in Render Dashboard

### 5. CORS Errors (API Calls Fail)

**Browser console shows:**

```
Access to XMLHttpRequest blocked by CORS policy
```

**Fix:**

1. Add frontend domain to Render Environment Variables:

   ```
   CORS_ALLOWED_ORIGINS=https://yourfrontend.com,https://braymell.onrender.com
   ```

2. Verify CORS middleware is enabled in settings.py:

   ```python
   MIDDLEWARE = [
       'corsheaders.middleware.CorsMiddleware',
       ...
   ]
   ```

3. Redeploy after changes

---

## 🟠 Database Issues

### 6. Database Connection Timeout

**Error:**

```
Error: could not connect to server: Connection timed out
```

**Causes:**

- Database is down
- Connection limit reached
- Network issue

**Fix:**

```bash
# 1. Check database status
# Go to Render Dashboard → PostgreSQL service
# Status should show "Available"

# 2. Restart database
# Click "Restart" button

# 3. Check connection string
# DATABASE_URL should be accessible
```

### 7. "Too Many Connections"

**Error:**

```
FATAL: sorry, too many clients already
```

**Fix:**

1. Reduce connection pool:

   ```python
   # In settings.py
   DATABASES = {
       'default': dj_database_url.config(
           conn_max_age=300  # Shorter timeout
       )
   }
   ```

2. Or upgrade Render PostgreSQL plan

3. Monitor connections:
   ```bash
   python manage.py dbshell
   SELECT count(*) FROM pg_stat_activity;
   ```

---

## ⚪ Deployment Issues

### 8. Build Script Fails

**Logs show:**

```
Build failed: bash build.sh returned non-zero exit code
```

**Check build.sh:**

```bash
#!/bin/bash
set -o errexit  # This causes it to exit on ANY error

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

**Fix:**

1. Check requirements.txt for invalid packages
2. Verify Python version matches runtime.txt
3. Check for typos in commands
4. Try building locally first:
   ```bash
   bash build.sh
   ```

### 9. Start Command Fails

**Procfile should have:**

```
web: gunicorn config.wsgi:application
```

**If it fails:**

1. Verify gunicorn is in requirements.txt ✅ (It is)
2. Verify config.wsgi exists and is valid
3. Check WSGI_APPLICATION setting:
   ```python
   # settings.py
   WSGI_APPLICATION = 'config.wsgi:application'
   ```

### 10. Deployment Stuck

**Deployment seems to hang**

**Fix:**

1. Wait 5-10 minutes (deployments can take time)
2. If still stuck, click **"Cancel Deploy"**
3. Try deploying again:
   - Click **"Deploy"** button
   - Or push new commit to GitHub

---

## 🟢 Optimization Issues

### 11. Slow Response Times

**Fix:**

1. **Optimize database queries:**

   ```python
   # Use select_related for foreign keys
   queryset = Client.objects.select_related('category')

   # Use prefetch_related for reverse relations
   queryset = Client.objects.prefetch_related('projects')
   ```

2. **Enable caching:**

   - Add Redis (Render can provision it)
   - Cache static responses

3. **Check Render metrics:**
   - CPU usage
   - Memory usage
   - Database load

### 12. Memory Issues

**Error:**

```
Killed - OOM (Out of Memory)
```

**Fix:**

1. Upgrade Render plan to higher tier
2. Optimize queries (remove N+1 problems)
3. Reduce pagination page size
4. Limit concurrent requests

---

## 🔧 Diagnostic Commands

### Access Render Shell

1. Web Service → Click **"Shell"** (top right)
2. Or from terminal if set up with Render CLI

### Useful Diagnostic Commands

```bash
# Check Python version
python --version

# List installed packages
pip list

# Check environment variables
env | grep -E "DATABASE|SECRET|CLOUDINARY"

# Test database connection
python manage.py dbshell

# Check migrations status
python manage.py showmigrations

# List database tables
python manage.py dbshell
\dt
\q

# Check static files
ls -la staticfiles/

# View recent logs
tail -100 /var/log/application.log
```

---

## 🆘 Emergency Recovery

### If Everything Breaks

**Step 1: Check logs**

```
Render Dashboard → Logs tab
Look for specific error messages
```

**Step 2: Rollback**

```bash
# Locally, revert to last working commit
git log --oneline
git reset --hard <commit-hash>
git push origin main
# Render will automatically redeploy
```

**Step 3: Check database**

```bash
# In Render Shell
python manage.py dbshell
SELECT version();  # Check DB is running
\q
```

**Step 4: Restart services**

1. Restart Web Service (Render Dashboard)
2. Restart PostgreSQL service
3. Wait 2-3 minutes
4. Test again

**Step 5: Contact support**

- Render Support: https://render.com/docs/support
- Include error logs

---

## 📋 Quick Diagnostic Checklist

Before contacting support, verify:

- [ ] **Logs checked** - Specific error identified
- [ ] **Environment variables** - All required ones set
- [ ] **Database running** - Check Render PostgreSQL status
- [ ] **Build script** - Tested locally with `bash build.sh`
- [ ] **Requirements.txt** - All packages listed
- [ ] **Git pushed** - Latest code on GitHub
- [ ] **No hardcoded values** - All config uses environment
- [ ] **Procfile correct** - Contains release and web commands
- [ ] **WSGI path** - Correct in Procfile

---

## 📞 Getting Help

1. **Check logs first** - 80% of issues are in logs
2. **Review this guide** - Most common issues covered
3. **Check Render status** - Is Render having outages?
4. **Restart everything** - Sometimes just needed
5. **Roll back** - Go to last known working version
6. **Contact Render support** - If still stuck

---

## 🚀 Quick Fixes (Try These First)

```bash
# 1. Update and redeploy
git add .
git commit -m "Force redeploy"
git push origin main

# 2. Manual deployment from Render
# Click "Deploy" button in Render Dashboard

# 3. Restart services
# Click "Restart" buttons for Web and Database

# 4. Clear cache and rebuild
# SSH to Render Shell and run:
python manage.py collectstatic --clear --noinput
```

---

## 📚 Additional Resources

- **Render Docs:** https://render.com/docs
- **Django Troubleshooting:** https://docs.djangoproject.com/en/4.2/faq/
- **PostgreSQL Help:** https://www.postgresql.org/docs/
- **Cloudinary Docs:** https://cloudinary.com/documentation

---

**Still stuck?** Check the main [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md) or contact Render support with your logs.

Good luck! 🎯
