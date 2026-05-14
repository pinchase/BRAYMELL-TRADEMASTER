# Local Development Setup Guide

## Prerequisites

- Python 3.11+ installed
- PostgreSQL installed and running
- pip (Python package manager)
- git

---

## Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/braymell.git
cd braymell/backend
```

---

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Step 4: Set Up Environment Variables

```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your actual values
nano .env
# or use your preferred editor
```

Update the following in `.env`:

```bash
# Django
SECRET_KEY=generate-a-secure-key-with-python
DEBUG=True  # True for development, False for production

# PostgreSQL Database
# If using local PostgreSQL:
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/braymell

# Or if using Supabase/external:
# DATABASE_URL=postgresql://user:password@host:5432/database

# Cloudinary (optional for development, required for production)
CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret

# Development CORS/CSRF settings
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CSRF_TRUSTED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### Generate SECRET_KEY

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## Step 5: Set Up PostgreSQL Database

### Option A: Using Docker (Recommended)

```bash
# Install Docker first, then run:
docker run --name braymell-db \
  -e POSTGRES_DB=braymell \
  -e POSTGRES_USER=braymell_user \
  -e POSTGRES_PASSWORD=your_password \
  -p 5432:5432 \
  -d postgres:15

# Update DATABASE_URL in .env:
DATABASE_URL=postgresql://braymell_user:your_password@localhost:5432/braymell
```

### Option B: Using Local PostgreSQL

```bash
# Connect to PostgreSQL
psql postgres

# In PostgreSQL shell:
CREATE DATABASE braymell;
CREATE USER braymell_user WITH PASSWORD 'your_password';
ALTER ROLE braymell_user SET client_encoding TO 'utf8';
ALTER ROLE braymell_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE braymell_user SET default_transaction_deferrable TO on;
ALTER ROLE braymell_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE braymell TO braymell_user;
\q
```

---

## Step 6: Run Migrations

```bash
# Activate virtual environment if not already active
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
```

Follow the prompts to create an admin user:

```
Username: admin
Email address: admin@example.com
Password: ••••••••
```

---

## Step 7: Collect Static Files (Development)

```bash
python manage.py collectstatic --noinput
```

---

## Step 8: Run Development Server

```bash
python manage.py runserver
```

The app will be available at: `http://localhost:8000`

Admin panel: `http://localhost:8000/admin/`

API Documentation: `http://localhost:8000/api/docs/`

---

## Useful Development Commands

### Database Management

```bash
# Run migrations
python manage.py migrate

# Make new migrations after model changes
python manage.py makemigrations

# View migration status
python manage.py showmigrations

# Reset database (WARNING: deletes all data)
python manage.py reset_db --noinput
```

### Django Shell (Interactive Python)

```bash
# Start Django shell
python manage.py shell

# Example usage in shell:
from core.models import Client, Project
clients = Client.objects.all()
print(clients)
```

### Create Test Data

```bash
# Create dummy data for testing
python manage.py shell
```

Then in the shell:

```python
from core.models import Client, Project, Testimonial
from django.utils.text import slugify

# Create a test client
client = Client.objects.create(
    name="Test Client",
    slug=slugify("Test Client"),
    description="A test client for development"
)

# Create a test project
project = Project.objects.create(
    title="Test Project",
    slug=slugify("Test Project"),
    client=client,
    description="A test project"
)

print("Test data created!")
```

### Static Files in Development

```bash
# Collect static files
python manage.py collectstatic

# Watch for changes (requires django-extensions)
python manage.py runserver_plus
```

---

## Troubleshooting Local Development

### 1. Database Connection Error

**Error:** `psycopg2.OperationalError: FATAL: database does not exist`

**Solution:**

```bash
# Check DATABASE_URL in .env is correct
# Make sure PostgreSQL is running
# Verify database name matches
psql -U braymell_user -d braymell -c "\dt"
```

### 2. Port 8000 Already in Use

**Error:** `Error: Address already in use`

**Solution:**

```bash
# Use a different port
python manage.py runserver 8001

# Or kill the process using port 8000
lsof -ti:8000 | xargs kill -9
```

### 3. Static Files Not Loading

**Error:** CSS/JS files return 404

**Solution:**

```bash
# Collect static files again
python manage.py collectstatic --clear --noinput

# Check STATIC_ROOT and STATIC_URL in settings.py
```

### 4. ModuleNotFoundError

**Error:** `ModuleNotFoundError: No module named 'X'`

**Solution:**

```bash
# Update requirements.txt
pip freeze > requirements.txt

# Install missing packages
pip install -r requirements.txt
```

### 5. Virtual Environment Not Activated

**Error:** Commands not found or wrong Python version

**Solution:**

```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Verify activation (should show (venv) in prompt)
```

---

## Making Changes to Models

When you modify model files:

```bash
# 1. Create migration file
python manage.py makemigrations

# 2. Review the generated migration (optional)
cat core/migrations/000X_*.py

# 3. Apply the migration
python manage.py migrate

# 4. Test the changes
python manage.py shell
```

---

## Testing the API

### Using curl:

```bash
# Get all projects
curl http://localhost:8000/api/v1/projects/

# Get single project
curl http://localhost:8000/api/v1/projects/1/

# Get all testimonials
curl http://localhost:8000/api/v1/testimonials/
```

### Using Postman:

1. Import collection from API Docs: `http://localhost:8000/api/docs/`
2. Create requests for endpoints
3. Test with different parameters

---

## Performance Tips

1. **Use Django Debug Toolbar:**

   ```bash
   pip install django-debug-toolbar
   # Add to INSTALLED_APPS in settings.py
   ```

2. **Database Query Optimization:**

   - Use `select_related()` for ForeignKeys
   - Use `prefetch_related()` for reverse relations
   - Use `.only()` to limit fields

3. **Static File Caching:**
   - Browser caches static files by default
   - Add version numbers to static URLs when updating

---

## Deploying to Production

When ready to deploy to Render:

1. Push code to GitHub:

   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```

2. Follow the **RENDER_DEPLOYMENT_GUIDE.md**

---

## Additional Resources

- **Django Documentation:** https://docs.djangoproject.com/
- **Django REST Framework:** https://www.django-rest-framework.org/
- **PostgreSQL Documentation:** https://www.postgresql.org/docs/
- **Render Documentation:** https://render.com/docs

---

## Need Help?

1. Check Django error messages carefully
2. Review logs: `python manage.py runserver` output
3. Check `.env` file is properly configured
4. Verify database is running
5. Check virtual environment is activated

Happy coding! 🚀
