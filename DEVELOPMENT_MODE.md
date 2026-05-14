# ✅ Development Mode - Configuration Summary

Your Braymell app is now fully configured for local development.

---

## 🔄 What Changed

### Settings (config/settings.py)

| Setting              | Before (Production)            | After (Development)          |
| -------------------- | ------------------------------ | ---------------------------- |
| **DEBUG**            | False                          | ✅ True                      |
| **SECRET_KEY**       | From environment               | ✅ Hardcoded development key |
| **ALLOWED_HOSTS**    | From environment               | ✅ localhost, 127.0.0.1, \*  |
| **DATABASE**         | PostgreSQL (via DATABASE_URL)  | ✅ SQLite (db.sqlite3)       |
| **CORS**             | Restricted to specific origins | ✅ localhost:3000, :8000     |
| **CSRF**             | HTTPS only                     | ✅ HTTP allowed              |
| **Security Headers** | Enabled                        | ✅ Disabled                  |

---

## 🗄️ Database Configuration

**Development Mode:**

```python
# Uses SQLite automatically
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

**How it works:**

- If `DEBUG=True` (development) → Uses SQLite
- If `DEBUG=False` and `DATABASE_URL` set (production) → Uses PostgreSQL

---

## 🚀 Quick Start (Restart Dev Server)

```bash
cd "/home/peterson/Desktop/braymell/BRAYMELLS (Copy 1)/backend"

# 1. Install dependencies (if needed)
pip install -r requirements.txt

# 2. Run migrations
python manage.py migrate

# 3. Start development server
python manage.py runserver
```

Or just run the start script:

```bash
bash start.sh
```

Access at: **http://localhost:8000**

---

## 🔧 Development Settings

### ALLOWED_HOSTS

```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]
```

✅ Allows all local connections

### CORS_ALLOWED_ORIGINS

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://127.0.0.1",
]
```

✅ Allows frontend dev servers

### CSRF_TRUSTED_ORIGINS

```python
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
```

✅ Allows local form submissions

### Security Headers

```python
if not DEBUG:
    # Production settings (all disabled in dev)
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
```

✅ All disabled since DEBUG=True

---

## 📝 Admin Panel

1. Create superuser (if needed):

   ```bash
   python manage.py createsuperuser
   ```

2. Access admin:
   - URL: http://localhost:8000/admin/
   - Use your superuser credentials

---

## 🧪 Testing

### Run Homepage

```bash
# Start server, then visit:
http://localhost:8000/
```

### Run Tests

```bash
python manage.py test
```

### Access API

```bash
# API Docs:
http://localhost:8000/api/docs/

# Create clients:
http://localhost:8000/api/v1/clients/

# Create projects:
http://localhost:8000/api/v1/projects/
```

---

## 🗂️ Database Files

### SQLite Database

```
db.sqlite3  ← Local development database
```

Changes are saved locally, no migrations needed for schema exploration.

### Media Files

```
media/  ← Uploaded files (local storage in dev)
```

In development, media is stored locally. In production, it uses Cloudinary.

---

## 🔄 Switching Back to Production

When ready to deploy to Render again:

1. **Set DEBUG to False:**

   ```python
   DEBUG = False
   ```

2. **Set environment variables on Render:**

   - `SECRET_KEY`
   - `DATABASE_URL`
   - `DEBUG=False`

3. **Deploy:**
   ```bash
   git add config/settings.py
   git commit -m "Switch to production mode"
   git push origin main
   ```

---

## ✨ Development Features Now Enabled

- ✅ **Detailed error pages** - Full stack traces in browser
- ✅ **Hot reload** - Changes reload automatically
- ✅ **SQLite database** - No PostgreSQL needed
- ✅ **CORS relaxed** - All localhost origins allowed
- ✅ **HTTP allowed** - No HTTPS required
- ✅ **Debug toolbar** - Can be added for request inspection
- ✅ **Static files** - Served automatically
- ✅ **Media files** - Stored locally

---

## 🚨 Important Notes

⚠️ **NEVER use these settings in production:**

- `DEBUG = True` exposes sensitive information
- Hardcoded `SECRET_KEY` is insecure
- All CORS origins allowed is a security risk
- HTTP-only is vulnerable

✅ **For production:**

- Keep DEBUG=False
- Use environment variables
- Restrict CORS to specific domains
- Always use HTTPS

---

## 📚 Related Files

- `config/settings.py` - Main configuration (updated)
- `build.sh` - Build script for Render
- `start.sh` - Development startup script
- `.env.example` - Environment variables template
- `LOCAL_SETUP.md` - Local development guide

---

## 🎯 You're Ready!

Your app is now in full development mode.

**Run this to start:**

```bash
bash start.sh
```

Or manually:

```bash
python manage.py runserver
```

Visit: **http://localhost:8000**

---

## ❓ Troubleshooting

### "Address already in use"

```bash
# Use different port
python manage.py runserver 8001
```

### "Database locked"

```bash
# Delete and recreate
rm db.sqlite3
python manage.py migrate
```

### "Static files not loading"

```bash
# Collect static files
python manage.py collectstatic
```

---

**Happy coding! 🚀**

Your development environment is ready to go!
